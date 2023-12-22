from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# 퀴즈 페이지 결과를 처리하는 엔드포인트
cnt = 0

@app.get("/get_cnt")
async def get_cnt():
    return {"cnt": cnt}
@app.post("/update_cnt/{increment}")
async def update_cnt(increment: int):
    global cnt
    cnt += increment
    print(f"Current cnt value: {cnt}")
    return {"cnt": cnt}
@app.post("/reset_cnt")
async def reset_cnt():
    global cnt
    cnt = 0
    return {"cnt": cnt}


from fastapi.responses import FileResponse

@app.get("/")
async def root():
    return FileResponse('index.html')

@app.get("/Q1")
async def root():
    return FileResponse('Q1.html')

@app.get("/Q2")
async def root():
    return FileResponse('Q2.html')
@app.get("/Q3")
async def root():
    return FileResponse('Q3.html')
@app.get("/Q4")
async def root():
    return FileResponse('Q4.html')
@app.get("/Q5")
async def root():
    return FileResponse('Q5.html')

@app.get("/INFO")
async def root():
    return FileResponse('INFO.html')
@app.get("/RE1")
async def root():
    return FileResponse('RE1.html')
@app.get("/RE2")
async def root():
    return FileResponse('RE2.html')
@app.get("/RE3")
async def root():
    return FileResponse('RE3.html')
@app.get("/RE4")
async def root():
    return FileResponse('RE4.html')
@app.get("/RE5")
async def root():
    return FileResponse('RE5.html')

@app.get("/agree")
async def root():
    return FileResponse('agree.html')
@app.get("/insert")
async def root():
    return FileResponse('insert.html')
@app.get("/thanks")
async def root():
    return FileResponse('thanks.html')

class ConsultationData(BaseModel):
    name: str
    phone: str
    content: str
@app.post("/send")
def post_consultation(data: ConsultationData):
    global cnt
    print(f"Received data: {data}")
    print(f"cnt: {cnt}, 이름: {data.name}, 연락처: {data.phone}, 상담 내용: {data.content}")

    # Insert data into the database
    db_insert(cnt, data.name, data.phone, data.content)

    return {"message": "전송완료"}



# Database connection parameters
db_config = {
    'host': '43.202.62.169',
    'user': '',
    'password': '',
    'database': 'tax-checker'
}

# taobao_product_id -> int
# naver_channel_name -> string
# naver_product_id -> int
# naver_title => string
# naver_category -> string

def db_insert(cnt, name, mobile, story):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Prepare the SQL insert statement
    insert_query = """
        INSERT INTO tax_checker (cnt, name, mobile, story) 
        VALUES (%s, %s, %s, %s)
        """
    values_to_insert = (cnt, name, mobile, story)

    # Execute the insert statement and commit the transaction
    cursor.execute(insert_query, values_to_insert)
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()