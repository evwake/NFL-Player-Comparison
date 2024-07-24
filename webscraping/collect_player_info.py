from bs4 import BeautifulSoup
import requests
import time
BASE_URL = "http://www.pro-football-reference.com"
PLAYER_URLS_BY_LETTER = [BASE_URL + "/players/" + chr(x) + "/" for x in range(65, 91)]

def parse_player(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    print(soup)


def parse_players_by_letter(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    all_players = soup.find("div", {"id": "all_players"}).find_all("a")
    for player in all_players:
        time.sleep(6)
        parse_player(BASE_URL + player.get("href"))

if __name__ == "__main__":
    for url in PLAYER_URLS_BY_LETTER:
        time.sleep(6)
        parse_players_by_letter(url)