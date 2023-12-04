from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (in a real application, use a database)
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
    return render_template('employee.html')

@app.route('/attendance-data')
def Attendance_data():
    return render_template('attendance-data.html')

@app.route('/salary-data')
def Salary_data():
    return render_template('salary-data.html')
@app.route('/reports-data')
def Reports_data():
    return render_template('reports-data.html')

if __name__ == '__main__':
    app.run(
        host= 'localhost',
        port= 8000,
        debug=True,
        load_dotenv= True)

