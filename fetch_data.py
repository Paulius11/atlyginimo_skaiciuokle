import re
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class Events:
    date_and_time: str
    open_spots: int
    link: str


def find_dates(text: str):
    "Parse dates and fallowing text (date) (text)"
    # create regex pattern
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) (.*)'
    # find all matches of the pattern in the text
    match = re.search(pattern, text)
    return match


def get_available_spots(text: str):
    """Return numbers from text"""
    pattern = r'^\D*(\d+)'
    match = re.search(pattern, text)
    if not match:
        return 0
    else:
        return match.group(1)


def get_events_at_night():
    """
    Get all events, that are happening at night
    :return:
    """
    url = "http://mao.tfai.vu.lt/400/"
    response = requests.get(url)
    # create BeautifulSoup object and parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # find all the div elements with class "div-1"
    div_elements = soup.findAll(True, {'class': ['div-1', 'div-2']})
    night_symbol = "â½"
    # iterate over the div elements and extract the desired text
    l_of_events = []
    for div in div_elements:
        is_night = not div.text.find(night_symbol)
        if is_night:
            match = find_dates(div.text)
            date: str = match.group(1)  # '2023-03-17 19:30'
            open_spots: int = int(get_available_spots(match.group(2)))
            link = url + div.parent.find("a").get("href")

            l_of_events.append(Events(date, open_spots, link))
    return l_of_events


