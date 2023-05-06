from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    location = request.form['location']
    bio = request.form['bio']

    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Location:", location)
    print("Bio:", bio)

    return 'Registration Successful!'

if __name__ == '__main__':
    app.run(debug=True)

