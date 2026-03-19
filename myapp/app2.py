from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', username=name)

@app.route('/users')
def users():
    user_list = ["kim", "lee", "park"]
    return render_template('index.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)