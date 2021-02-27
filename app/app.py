import const
from mappi_manager import MappiManager
from flask import Flask, redirect

app = Flask(__name__)

mm = MappiManager(const.MAPPI_FILENAME)


@app.route("/reload")
def reload():
    mm.reload_mappi_dict()
    return "Reloaded Successfully"


@app.route("/<nickname>")
def go_to_nickname(nickname):
    nickname = nickname.lower()
    data = mm._mappi.get(nickname)
    if not data:
        return "{} nickname does not exist".format(nickname)
    return redirect(data["default"])


@app.route("/<nickname1>/<nickname2>")
def go_to_nickname12(nickname1, nickname2):
    nickname1 = nickname1.lower()
    nickname2 = nickname2.lower()

    data = mm._mappi.get(nickname1)
    if not data:
        return "{} nickname does not exist".format(nickname1)

    url = data["default"]
    data2 = data.get(nickname2)
    if not data2:
        url += data.get("suffix", "") + nickname2
    else:
        url += data.get("prefix", "") + data2["default"]
    return redirect(url)


if __name__ == "__main__":
    app.run("0.0.0.0")
