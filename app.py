from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/department/<dept>')
def department(dept):
    # Implement logic to display department-specific teacher details
    # You might use a database or data structure to store teacher information
    return render_template('department.html', department=dept, logged_in=False)


@app.route('/teacher/<teacher_id>')
def teacher(teacher_id):
    # Display individual teacher details
    # Implement logic to fetch teacher data by ID
    # You can also check if the user is logged in to display additional details
    return render_template('teacher.html', logged_in=False)


# A simple in-memory dictionary to store user data. In a real application, you would use a database.
users = {}


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            return "Username already exists. Please choose a different one."

        # In a real application, you would hash and securely store the password.
        users[username] = password
        return "Registration successful. You can now <a href='/login'>login</a>."

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            # User is authenticated, set a session variable or use a secure token for session management.
            return "Login successful. You can now <a href='/attendance'>Courses</a>."
        else:
            return "Invalid username or password. Register first. <a href='/register'>Register</a>."

    return render_template('login.html')


@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/takeattendance')
def attendance():
    return render_template('takeattendance.py')

if __name__ == '__main__':
    app.run(debug=True)
