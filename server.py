from flask import Flask, jsonify
from loginApi import LoginApi
app = Flask(__name__)

# instiate our loginApi object
loginApi = LoginApi()

@app.route("/test")
def test():
    return jsonify({"status":"server is running"})


if __name__ == '__main__':
    loginApi.checkUserPass("exsample","example")
    app.run()