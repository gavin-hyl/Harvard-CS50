import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = list(set(
            link for link in pages[filename]
            if link in pages
        ))

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    model = dict()
    for p in corpus:
        model[p] = (1-damping_factor) / len(corpus)
    for p in corpus[page]:
        model[p] += damping_factor / len(corpus[page])
    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page = random.choice(list(corpus.keys()))
    result = dict((p, 0) for p in corpus)
    for _ in range(n):
        t_model = transition_model(corpus, current_page, damping_factor)
        t_list = random.choices(population=list(t_model.keys()), weights=list(t_model.values()))
        current_page = random.choice(t_list)
        result[current_page] += 1
    for page in result:
        result[page] /= n
    return result


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    thresh = 0.001
    corp_len = len(corpus)
    result = dict((p, 1 / corp_len) for p in corpus)
    continue_flag = True
    while continue_flag:
        continue_flag = False
        for p in corpus:
            sum = 0
            for psum in corpus:
                sum += result[psum] * (p in corpus[psum]) / len(corpus[psum])
            new_pr = (1-damping_factor) / corp_len + damping_factor * sum
            if abs(new_pr - result[p]) > thresh:
                continue_flag = True
            result[p] = new_pr
    return result

if __name__ == "__main__":
    main()
