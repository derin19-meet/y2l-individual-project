
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method=='POST':
		link=request.form['link']
		add_pic(link)
		print( "Success")
		return redirect(url_for('main'))

	else:
		return render_template('add.html')
@app.route('/main')
def main():
	doggoes=get_all()
	return render_template("main.html", doggoes=doggoes)


if __name__=='__main__':
	app.run(debug=True)




