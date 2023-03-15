from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/hours/')
def hours():
    return render_template('hours.html')

@app.route('/hazmat/')
def hazmat():
    return render_template('hazmat.html')

@app.route('/batteries/')
def batteries():
    return render_template('batteries.html')

if __name__ == "__main__":
    app.run(debug=True)