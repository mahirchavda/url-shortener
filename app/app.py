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
    url = mm.get_long_url(nickname)
    if not url:
        return "{} nickname does not exist".format(nickname)
    return redirect(url)


if __name__ == "__main__":
    app.run("0.0.0.0")
