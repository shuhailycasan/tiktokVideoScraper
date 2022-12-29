from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def downloadVideo(link, id):
    cookies = {
        '__cflb': '02DiuEcwseaiqqyPC5pEJ2ZMVzJMMdZ5xAV8NwVWR1Zqd',
        '_ga': 'GA1.2.849519689.1672296165',
        '_gid': 'GA1.2.23818797.1672296165',
        '__gads': 'ID=8fccf1449f88b3da-226d0c4713d900b5:T=1672296164:RT=1672296164:S=ALNI_MaAOOtRjYcrqKgZpnYN-vE6eXlQUA',
        '__gpi': 'UID=00000b9a277a6033:T=1672296164:RT=1672296164:S=ALNI_MZF09hDBRSzDK08bHz0_y2VoET8Ag',
        'FCNEC': '%5B%5B%22AKsRol-MKe18r8AtS5Jth-9spfxkAn_pObT0RHtrfvClCXbfGxxIsIDm9nVBYLAprlfPIHxLUoxOgzF6cxYq8IZlytMamW15OVnZIxv8UFrqUS4vO9qmX6FQjRA4OyX3iNjjB1ZvppOBpndZ8QmaF6tMeUEtJvxbbQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=02DiuEcwseaiqqyPC5pEJ2ZMVzJMMdZ5xAV8NwVWR1Zqd; _ga=GA1.2.849519689.1672296165; _gid=GA1.2.23818797.1672296165; __gads=ID=8fccf1449f88b3da-226d0c4713d900b5:T=1672296164:RT=1672296164:S=ALNI_MaAOOtRjYcrqKgZpnYN-vE6eXlQUA; __gpi=UID=00000b9a277a6033:T=1672296164:RT=1672296164:S=ALNI_MZF09hDBRSzDK08bHz0_y2VoET8Ag; FCNEC=%5B%5B%22AKsRol-MKe18r8AtS5Jth-9spfxkAn_pObT0RHtrfvClCXbfGxxIsIDm9nVBYLAprlfPIHxLUoxOgzF6cxYq8IZlytMamW15OVnZIxv8UFrqUS4vO9qmX6FQjRA4OyX3iNjjB1ZvppOBpndZ8QmaF6tMeUEtJvxbbQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'S2tzREE5',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]

    mp4File = urlopen(downloadLink)
    with open(f"videos/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/@codewithvincent")

time.sleep(1)

scroll_pause_time = 4
screen_height = driver.execute_script("return window.screen.height;")
i = 4

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height = screen_height, i = i))
    i += 4
    time.sleep(scroll_pause_time)

    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source,"html.parser")
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))

for index, video in enumerate(videos):
    downloadVideo(video.a["href"], index)
    time.sleep(10)

