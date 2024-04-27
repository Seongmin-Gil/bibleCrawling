# -*- coding: utf-8 -*-

import requests
import re
import os
from bs4 import BeautifulSoup

bible_title = {
    "창세기": "gen",
    "출애굽기": "exo",
    "레위기": "lev",
    "민수기": "num",
    "신명기": "deu",
    "여호수아": "jos",
    "사사기": "jdg",
    "룻기": "rut",
    "사무엘상": "1sa",
    "사무엘하": "2sa",
    "열왕기상": "1ki",
    "열왕기하": "2ki",
    "역대상": "1ch",
    "역대하": "2ch",
    "에스라": "ezr",
    "느헤미아": "neh",
    "에스더": "est",
    "욥기": "job",
    "시편": "psa",
    "잠언": "pro",
    "전도서": "ecc",
    "아가": "sng",
    "이사야": "isa",
    "예레미야": "jer",
    "예레미야애가": "lam",
    "에스겔": "ezk",
    "다니엘": "dan",
    "호세아": "hos",
    "요엘": "jol",
    "아모스": "amo",
    "오바댜": "oba",
    "요나": "jnh",
    "미가": "mic",
    "나훔": "nam",
    "하박국": "hab",
    "스바냐": "zep",
    "학개": "hag",
    "스가랴": "zec",
    "말라기": "mal",
    "마태복음": "mat",
    "마가복음": "mrk",
    "누가복음": "luk",
    "요한복음": "jhn",
    "사도행전": "act",
    "로마서": "rom",
    "고린도전서": "1co",
    "고린도후서": "2co",
    "갈라디아서": "gal",
    "에베소서": "eph",
    "빌립보서": "php",
    "골로새서": "col",
    "데살로니가전서": "1th",
    "데살로니가후가": "2th",
    "디모데전서": "1ti",
    "디모데후서": "2ti",
    "디도서": "tit",
    "빌레몬서": "phm",
    "히브리서": "heb",
    "야고보서": "jas",
    "베드로전서": "1pe",
    "베드로후서": "2pe",
    "요한1서": "1jn",
    "요한2서": "2jn",
    "요한3서": "3jn",
    "유다서": "jud",
    "요한계시록": "rev",
}


def get_crawling_data(URL, vol, chap):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    data = requests.get(URL)
    soup = BeautifulSoup(data.text, "html.parser")

    datas = soup.find("div", class_="wide")
    texts = datas.get_text().split("\n")

    texts = [value for value in texts if value]

    if not texts:
        print("존재하지 않습니다.")
        return

    filePath = os.getcwd()
    fileName = "/dbible_{}_{}장.txt".format(vol, chap)
    print(filePath + fileName)
    file = open(filePath + fileName, "w", encoding="UTF8")

    for text in texts:
        num = re.findall(r"\d+", text)
        text = text.replace(num[0], "{}{}".format(num[0], " "))
        text = text + "\n"

        file.write(text)

        print(text)

    file.close()


while True:
    print("찾고자하는 성경말씀을 입력하세요.(ex : 창세기)")

    vol = input()
    input_vol = bible_title.get(vol)
    if input_vol == None:
        print("존재하지 않습니다.")
    else:
        print("{0}의 몇장을 찾으시나요.".format(vol))

        input_chap = input()

        search_bible_url = "http://bible.godpia.com/read/reading.asp?calDate=&seq=1&ver=easy&ver2=&vol={0}&chap={1}&vol2=&chap2=#gobody".format(
            input_vol, input_chap
        )

        get_crawling_data(search_bible_url, vol, input_chap)

    print("종료하시겠습니까? (yes = y, no = Press any key)")
    answer = input()
    if answer == "y":
        break
