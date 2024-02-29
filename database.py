from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Cloudflare290'
app.config['MYSQL_DB'] = 'emp'

mysql = MySQL(app)
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM ')
    data = cursor.fetchall()
    cursor.close()
    return str(data)
if __name__ == '__main__':
    app.run(debug=True)
# Replace 'username', 'password', 'hostname', and 'database_name' with your MySQL credentials
# engine = create_engine('mysql+pymysql://root:Cloudflare290@/emp?charset=utf8mb4')




# engine = create_engine("mysql+pymsql://root:Cloudflare90@/emp?charset=utf8mb4")