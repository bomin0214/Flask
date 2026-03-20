from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

# 홈 페이지
@app.route('/home')
def home():
    return render_template('home.html')

# 결과 페이지
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)