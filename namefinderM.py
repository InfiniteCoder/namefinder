from multiprocessing.dummy import Pool as ThreadPool

import requests

# Set these variables
num_threads = 10
wordfile = "/usr/share/dict/cracklib-small"


def check(parse_url, parse_word):
    """
    check if subdomain is available
    :param parse_url: url to be checked
    :param parse_word: word used
    """
    payload = {
        "Host": "api.heroku.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Accept": "application/vnd.heroku+json; version=3",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://dashboard.heroku.com/",
        "X-Heroku-Requester": "dashboard",
        "Origin": "https://dashboard.heroku.com",
        "DNT": "1",
        "Connection": "keep-alive"
    }
    response = requests.get(url=parse_url, headers=payload)
    if response.status_code == 404:
        print(parse_word)


url = "https://api.heroku.com/apps/"
urls = []
valid_words = []
# read from dictionary and create urls
words = open(wordfile, "r")
for word in words:
    word = word.rstrip()
    if word.isalnum() and word[0].isalpha() and len(word) >= 3:
        urls.append(url + word)
        valid_words.append(word)

pool = ThreadPool(num_threads)
pool.starmap(check, zip(urls, valid_words))
pool.close()
pool.join()
