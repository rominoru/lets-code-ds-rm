from flask import Flask
from sqlalchemy import create_engine, text
from datetime import datetime
import re

app = Flask(__name__)
db_url = "mssql+pymssql://sa:mag@localhost:1433/maryflix"
# A cadeia de conexão é formada por  dialect[+driver]://user:password@host:port/dbname
engine = create_engine(db_url, pool_size=5, pool_recycle=3600)


conn = engine.connect()
sql_text = text("SELECT * FROM dbo.usuarios")
result = conn.execute(sql_text)
print(f"Number of rows = {result.rowcount}.")

for row in result:
    print(row)
conn.close()

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    conn = engine.connect()
    sql_text = text("SELECT * FROM dbo.usuarios")
    result = conn.execute(sql_text)

    content = ''
    for row in result:
        content = content + str(row)
    conn.close()
    return content
