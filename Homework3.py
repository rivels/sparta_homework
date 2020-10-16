import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta    # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#곡 제목 링크
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#아티스

Rows=soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in Rows:
    title= song.select_one('td.info > a.title.ellipsis').text
    rank= (song.select_one('td.number').text)[0:2]
    artist=song.select_one('td.info > a.artist.ellipsis').text
    print(rank.strip(),title.strip(),artist.strip())
    doc ={'rank':rank.strip(),
          'title':title.strip(),
          'aritist':artist.strip()}
    db.songs.insert_one(doc)