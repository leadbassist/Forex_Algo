from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_article(data):
    return dict(
        headline=data.get_text(), link="https://www.bloomberg.com" + data["href"]
    )


def bloomberg_com():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    }

    resp = requests.get("https://www.bloomberg.com/fx-center", headers=headers)

    soup = BeautifulSoup(resp.content, "html.parser")

    headline = soup.select_one(".single-story-module__headline-link")

    # print(headline)

    all_links = []
    all_links.append(get_article(headline))

    grid_articles = soup.select(".grid-module-story__headline-link")
    [all_links.append(get_article(x)) for x in grid_articles]

    side_articles = soup.select(".story-list-story__info__headline-link")
    [all_links.append(get_article(x)) for x in side_articles]

    return all_links
