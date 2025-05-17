import csv
import requests
from bs4 import BeautifulSoup

URL = "https://db.netkeiba.com/?pid=horse_top"


def scrape_horse_data(url: str = URL):
    """Scrape horse data from netkeiba without using Selenium."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    names = [a.get("title", a.get_text(strip=True))
             for a in soup.select('#contents_liquid > div > form > table > tbody > tr > td.bml.txt_l > a')][:20]
    genders_birth = [td.get_text(strip=True)
                     for td in soup.select('#contents_liquid > div > form > table > tbody > tr > td.txt_c')][:40]
    others = [td.get_text(strip=True)
              for td in soup.select('#contents_liquid > div > form > table > tbody > tr > td.txt_l')][:120]

    return names, genders_birth, others


def save_csv(filename: str, rows):
    """Write list of rows to csv."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([[row] for row in rows])


def main():
    names, genders_birth, others = scrape_horse_data()
    save_csv("name.csv", names)
    save_csv("gen_born.csv", genders_birth)
    save_csv("others.csv", others)


if __name__ == "__main__":
    main()
