from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!'


# @app.route('/favicon.ico')
# def new_blog():
#     return 'These is favicon.io'


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog!'

# TODO: to run the code: in 'web server' folder Scripts\activate.bat; set FLASK_APP=server.py; flask run;

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'] )
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again!'
