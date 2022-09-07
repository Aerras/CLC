from flask import Flask, render_template, url_for, request, session
from sendMail import send_email
import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SK

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about', methods=["POST", 'GET'])
def about():

    if request.method == 'POST':
        send_email(request.form['email'], request.form['message'])


    return render_template('about.html')


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')




if __name__ == '__main__':
    app.run(debug=True)
