from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.json.ensure_ascii = False

Swagger(app)

@app.route("/api/hello")
def hello():
    """
    간단한 Hello API
    ---
    responses:
      200:
        description: 성공 메시지 반환
        examples:
          application/json:
            message: 성공
    """

    return jsonify({
    "message": "성공"
})

if __name__ == "__main__":
    app.run(debug=True)