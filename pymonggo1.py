from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
# print(target_movie['star'])
target_star = target_movie['star']

movies = list(db.movies.find({'star': target_star}))

for movie in movies:
    db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})
    print(movie['title'],movie['star'])