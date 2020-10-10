from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(' https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
#old_content > table > tbody > tr
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
movies = soup.select('#old_content > table > tbody > tr')
#############################
# (입맛에 맞게 코딩)
#############################
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# for movie in movies:
#
    # atag = movie.select_one("td.title > div > a")
    # if atag is not None:
    #     rank = movie.select_one("td:nth-child(1) > img")['alt']
    #     title=atag.text
    #     star=movie.select_one('td.point').text
    #     print(rank,title,star)
for movie in movies:
    atag=movies.select_one("td.title > div > a")
    if atag is not None:
        rank=movie.select_one("td:nth-child(1) > img")['alt']
        title=atag.text
        star=movie.select_one('td.point').text

        doc ={
            "rank":rank,
            "title":title,
            "star":star
        }
        db.movies.insert_one(doc)




# MongoDB에서 데이터 모두 보기
# all_users = list(db.users.find_one({'age':85}))
# all_users = db.users.find_one({'age':85})
# print(all_users)

# for i in all_users:
#     print(i['name'])





