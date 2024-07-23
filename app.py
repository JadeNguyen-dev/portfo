from flask import Flask, render_template, url_for, redirect
from flask import request
import csv

app = Flask(__name__)


# @app.route("/<username>/<int:postid")
# def hello_world(username=None, postid=0):
#     return render_template('index.html', name=username, postid=postid)


@app.route("/")
def hello_world():
    return render_template('index.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route('/works.html')
# def blog2():
#     return render_template('works.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save data to database"
    return 'something wrong happened'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
