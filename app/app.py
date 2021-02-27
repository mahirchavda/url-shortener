import logging
from flask import Flask, redirect, request

import const
from mappi_manager import MappiManager
from errors import ShortURLNotFound
from log_manager import Logger

app = Flask(__name__)

logger = Logger.get_logger("url-shortener")

mm = MappiManager(const.NICKNAME_FILE, const.MAPPI_FILE)

ACCESS_LOG = "remote_addr={}, method={} path={}, response={}, user_agent={},"


@app.before_request
def handle_all():
    if request.path == "/favicon.ico":
        return "Not Found"
    try:
        url = mm.get_redirect_url(request.path)
        logger.info(
            ACCESS_LOG.format(
                request.remote_addr,
                request.method,
                request.path,
                "Redirecting to::{}".format(url),
                request.user_agent,
            )
        )
        return redirect(url)
    except ShortURLNotFound as err:
        logger.info(
            ACCESS_LOG.format(
                request.remote_addr,
                request.method,
                request.path,
                "Not Found::{}".format(err),
                request.user_agent,
            )
        )
        return str(err)
    except Exception as err:
        response = "Unknown error occured: {}".format(err)
        logger.error(
            ACCESS_LOG.format(
                request.remote_addr,
                request.method,
                request.path,
                "Error::{}".format(response),
                request.user_agent,
            )
        )
        logger.exception(err)
        return response


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
