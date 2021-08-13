from flask import Flask, request, session, redirect, render_template
app = Flask(__name__)
app.secret_key = 'ajgawfd762512hqdjwgs3'

@app.route('/')
def index():
    if "visits" not in session:
        session['visits'] = 0
    else:
        session['visits'] = session['visits'] + 1
    return render_template('index.html')

@app.route('/add_two_visits')
def two_visits():
    if "visits" not in session:
        session['visits'] = 0
    else:
        session['visits'] = session['visits'] + 1
    return redirect('/')

@app.route('/reset_session')
def destroy_session():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)