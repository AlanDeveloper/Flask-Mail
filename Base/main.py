from flask import Flask, flash, render_template, request, redirect, url_for, session
from server import ServerDAO

app = Flask(__name__, template_folder='template')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def reg():
    ServerDAO().subscribe(request.form['email'])
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		result = ServerDAO().login(request.form['email'], request.form['password'])

		if result == None:
			flash('Dados incorretos')
			return redirect(url_for('login'))
		else:
			session['username'] = request.form['email'].split('@')[0]
			session['password'] = request.form['password'] 
			return redirect(url_for('feed'))
	
	if 'username' not in session:
		return render_template('login.html')
	else:
		return redirect(url_for('feed'))

@app.route('/loggout')
def loggout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/feed', methods=['GET', 'POST'])
def feed():
	if request.method == 'POST':
		result = ServerDAO().send(session['username'], request.form['message'])
		if result:
# 			

		return redirect(url_for('feed'))
	return render_template('feed.html')

if __name__ == '__main__':
	app.run(debug=True)
