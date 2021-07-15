from flask import Flask, request, render_template
from dao import bank_get2

app = Flask(__name__)

# index.html 단순 실행
# http://ip:port/
@app.route("/", methods=["get"])
def index_view():
    return render_template("index.html")


# 버튼 클릭시에 비동기로 응답
@app.route("/dataget", methods=["get"])
# def req_res():
#     data =  bank_get2()

#     print("-----", type(data))
#     print(dict(data))  # {'key': 'doc_count'} 재선
#     return dict(data)

# 유지현작

#응답된 데이터 첫번째 형식
# js에서 문제 발생
# json 포멧으로 변환하려는 두가지 방식 다 실패
# JSON.parse(문자열) : key와 value의 구조는 큰따옴표 표기 필수 -> JSON 객체로 변환
# eval("(" + 문자열 + ")") -> JSON 객체로 변환
#{'key': 235, 'doc_count': 1}{'key': 784, 'doc_count': 1}{'key': 971, 'doc_count': 1}{'key': 1002, 'doc_count': 1}{'key': 1506, 'doc_count': 1}{'key': 2543, 'doc_count': 1}{'key': 3912, 'doc_count': 1}{'key': 4121, 'doc_count': 1}{'key': 4513, 'doc_count': 1}
# 어~~ js에서 함수로 처리 불가 
# 해결책 :  {},{} 여러개 즉 하나이상인 경우 json 배열 형식이어야 함, json 배열 형식의 문자열로 변환시도
# 첫번째 방식 : index.html의 js 코드에서 해결
# 두번째 방식 : python 코드에서 [ ] 결합 추가 

def req_res():
    data = bank_get2()
    str_data = ""
    for i in range(len(data)):
        str_data += str(data[i]) + ","
    return str_data

# 이홍주 작 return str(data)

if __name__== "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

'''

index.html -> 버튼 클릭하면 ES의 결과값을 받아서 화면에 table을 동적으로 생성 

소스의 실행 구조
- 비동기 
app.py -> index.html -> 버튼 클릭 -> app.py 
-> dao.py 의 bank_get2() 결과값 리턴받아서 -> app.py -> index.html

'''
