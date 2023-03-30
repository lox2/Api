from flask import Flask, render_template, request
import os
import json
import utils

app = Flask(__name__)


@app.route("/")
def index_route():
    return render_template("index.html")


@app.route("/forgot")
def forgot_route():
    return render_template("forgot.html")


@app.route("/main")
def main_page():
    return render_template("main.html")


@app.route("/add_food")
def add_food():
    return render_template("addfood.html")


@app.route("/add_train")
def add_train():
    return render_template("addzan.html")


@app.route("/api/login_pass", methods=['POST'])
def login_pass():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return utils.check_user(data["username"], data["password"])


@app.route("/api/register", methods=['POST'])
def register():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    print(utils.register(data["username"], data["password"]))
    return utils.register(data["username"], data["password"])


@app.route("/api/change_password", methods=['POST'])
def change_password():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return {"ok": utils.change_password(data["username"], data["password"])}


@app.route("/api/add_food", methods=['POST'])
def api_add_food():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return {"ok": utils.add_food(data["id"], data["food"], data["date"])}


@app.route("/api/add_train", methods=['POST'])
def api_add_train():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return {"ok": utils.add_train(data["id"], data["train"], data["date"])}


@app.route("/api/remove_train", methods=['POST'])
def api_remove_train():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return utils.remove_train(data["id"], data["train"], data["date"])


@app.route("/api/remove_food", methods=['POST'])
def api_remove_food():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return utils.remove_food(data["id"], data["food"], data["date"])


@app.route("/api/get_trains", methods=['POST'])
def api_get_trains():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return utils.get_trains(data["id"], data["date"])


@app.route("/api/get_food", methods=['POST'])
def api_get_food():
    if not request.data:
        raise Exception
    data = json.loads(request.data)
    return utils.get_food(data["id"], data["date"])


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
