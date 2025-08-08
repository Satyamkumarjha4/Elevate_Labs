"""
Task 3 : Web Scraper for News Headlines.
Objective: Scrape top headlines from a news website.
Tools : Python, requests, BeautifulSoup
Deliverables: Python script + .txt file of headlines

Hints/Mini Guide:
1.Use requests to fetch HTML
2.Use BeautifulSoup to parse <h2> or title tags
3.Save the titles in a .txt file

Outcome: : Automate data collection from a public website
"""

import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from requests.exceptions import RequestException

init(autoreset=True)


class NewsScraper:
    def __init__(self, url=None, class_name='p-url', filename='Web-Scraper/headlines.txt'):
        self.url = url or 'https://thrivenews.co'
        self.class_name = class_name
        self.filename = filename
        self.headlines = []

    def fetch_headlines(self):
        print(Fore.CYAN + f"Fetching headlines from {self.url} with class '{self.class_name}'...")
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(class_=self.class_name)

            headlines = [el.get_text(strip=True) for el in elements if el.get_text(strip=True)]
            self.headlines = list(dict.fromkeys(headlines))  # Remove duplicates

            if not self.headlines:
                print(Fore.YELLOW + f"No content found with class '{self.class_name}'.")
            else:
                print(Fore.GREEN + f"Successfully scraped {len(self.headlines)} headlines.")

        except RequestException as e:
            print(Fore.RED + f"Error fetching data: {e}")
        except Exception as e:
            print(Fore.RED + f"Unexpected error during parsing: {e}")

    def save_headlines(self):
        if not self.headlines:
            print(Fore.YELLOW + "No headlines to save.")
            return

        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write("📰 Scraped Headlines from {}\n".format(self.url))
                file.write("-" * 50 + "\n")
                for idx, headline in enumerate(self.headlines, start=1):
                    file.write(f"{idx}. {headline}\n")
            print(Fore.GREEN + f"Saved {len(self.headlines)} formatted headlines to '{self.filename}'.")

        except IOError as e:
            print(Fore.RED + f"Failed to write to file: {e}")


    def run(self):
        self.fetch_headlines()
        self.save_headlines()


if __name__ == "__main__":
    scraper = NewsScraper(
        url='https://thrivenews.co',  # Target site
        class_name='p-url',           # Class to search
        filename='Web-Scrapper/headlines.txt'
    )
    scraper.run()
