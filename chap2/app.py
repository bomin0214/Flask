from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    num = int(request.form['number'])

    if num >= 90:
        grade = "A"
    elif num >= 70:
        grade = "B"
    else:
        grade = "C"

    numbers = list(range(1, num + 1))

    return render_template('result.html', grade=grade, numbers=numbers, num=num)

if __name__ == '__main__':
    app.run(debug=True)