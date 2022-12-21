#!/usr/bin/python3
""" Count it module """
import requests


def count_words(subreddit, word_list, after="", word_counter=None):
    """
    Function sorted by number of occurences and
    alphabetically for each article
    Arguments:
        - subreddit: subreddit to search
        - word_list: list of words to search for
        - after: after parameter for pagination
        - word_counter: dictionary of words and their count
    Returns:
        - None if subreddit is invalid or no posts match
    """
    if after is None:
        return None
    if word_counter is None:
        word_counter = {}
        for word in word_list:
            word_counter[word] = 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    params = {
        "limit": 100,
        "after": after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    response = response.json()
    data = response.get("data")
    after = data.get("after")
    posts = data.get("children")
    for post in posts:
        post = post.get("data")
        title = post.get("title").lower()
        title = title.replace(".", " ").replace("!", " ").replace("_", " ")
        title = title.split(" ")
        for word in title:
            if word in word_counter:
                word_counter[word] += 1
    count_words(subreddit, word_list, after, word_counter)
    if after is None:
        for word in sorted(word_counter, key=word_counter.get, reverse=True):
            if word_counter[word] != 0:
                print("{}: {}".format(word, word_counter[word]))
