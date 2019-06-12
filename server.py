from flask import Flask, jsonify, request
from loginApi import LoginApi
app = Flask(__name__)

# instiate our loginApi object
loginApi = LoginApi()

@app.route("/test")
def test():
    return jsonify({"status":"server is running"}),200

@app.route("/isUser",methods=['POST'])
def isUser():
    if(request.data):
        jsonData = request.get_json()
        username = jsonData['username']
        password = jsonData['password']
        isUser = loginApi.isUser(username,password)
        isAdmin = loginApi.isAdmin(username)
        return jsonify({"valid":isUser,"isAdmin":isAdmin}),200

if __name__ == '__main__':
   app.run()