import requests
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

# 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
city_air = response_data.json()
gus = city_air['RealtimeCityAir']['row']

for gu in gus:
    if gu['PM10']<20:
        print(gu['MSRSTE_NM'],gu['PM10'])