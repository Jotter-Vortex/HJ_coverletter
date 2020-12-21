#from bson import ObjectId
from flask import Flask, render_template
#, jsonify, request, sessions
#import requests
#from bs4 import BeautifulSoup
#from pymongo import MongoClient                 # pymongo를 import하기
#import datetime                                     # 현재 시간을 가져오기 위함.

app = Flask(__name__)

#client = MongoClient('mongodb://changjin:0001@13.209.47.213', 27017)        # mongoDB는 27017 포트로 돌아감
#db = client.my_invent                            # 'notepad'라는 이름의 db를 생성함

## HTML을 주는 부분
@app.route('/')                                 # home 주소
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)