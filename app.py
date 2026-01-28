# app.py
from flask import Flask, render_template

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# PROJECT CATEGORY PAGES
@app.route('/graphics')
def graphics():
    return render_template('graphics.html')

@app.route('/ai-ml')
def ai_ml():
    return render_template('ai.html')

@app.route('/data-science')
def data_science():
    return render_template('data.html')

@app.route('/game-dev')
def game_dev():
    return render_template('games.html')

if __name__ == '__main__':
    app.run(debug=True)
