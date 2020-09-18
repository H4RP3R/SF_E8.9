import requests
import re
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, url):
        self.url = url
        self.page = None

    def get_page(self):
        err = None
        try:
            self.page = requests.get(self.url, timeout=0.005)
        except ConnectionError as err:
            self.error = err

        return err

    def count_matches(self):
        '''Returns the page status code and the number of matches.'''
        soup = BeautifulSoup(self.page.content, 'html.parser')
        regex = re.compile('\Wpython\W')
        page_text = soup.get_text().lower()
        matches = re.findall(regex, page_text)
        return self.page.status_code, len(matches)
