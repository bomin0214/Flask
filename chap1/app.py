from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route('/result', methods = ['POST'])
def result():
    name = request.form['username']
    users = ["kim", "lee", "park", name]

    return render_template(
        'result.html',
        username = name,
        users=users
    )

if __name__ == '__main__':
    app.run(debug=True)