from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Cloudflare290'
app.config['MYSQL_DB'] = 'emp'

mysql = MySQL(app)

# Dummy user data (in a real application, it will be a database)
users = {'admin': '1234'}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('login'))
@app.route('/employee-data')
def Employee_data():
    print("Fetching employee data...")
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM employees')
    
    # Get column names
    columns = [col[0] for col in cursor.description]
    
    # Fetch data and convert each row to a dictionary
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    # print("Fetched data:", data)
    
    return render_template('employee.html', data=data)


# @app.route('/reports-data')
# def Reports_data():
#     return render_template('reports-data.html')

if __name__ == '__main__':
    app.run(
        host= 'localhost',
        port= 8000,
        debug=True,
        load_dotenv= True)
