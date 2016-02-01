from flask import Flask
app = Flask(__name__)

@app.route("/verbs/get_verbs/user_id/<int:user_id>", methods = ["GET"])
def getVerbs(user_id = None):
    return "Verbos para el usuario : " + user_id

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
