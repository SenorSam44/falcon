"""Python Flask WebApp Auth0 integration example
    otp = totp.now()
"""
import json
import traceback

from flask import Flask, request, redirect, render_template, session, url_for, jsonify
from flask_cors import cross_origin
from dotenv import find_dotenv, load_dotenv
from os import environ as env
from urllib.parse import quote_plus, urlencode
from werkzeug.exceptions import HTTPException

from utils.logger import app_logger

# ENV
# 👆 We're continuing from the steps above. Append this to your project.py file.

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Flask
app = Flask(__name__, static_url_path="/rest/static", static_folder="static")
app.logger.critical("env file = " + str(ENV_FILE))
app_logger = app_logger()

app.debug = True


@app.after_request
def log_after_request(response):
    app_logger.info(
        "path: %s | method: %s | status: %s",
        request.path,
        request.method,
        response.status,
    )

    return response


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    log_msg = f"HTTPException {e.code}, Description: {e.description}, Stack trace: {traceback.format_exc()}"
    app_logger.error(msg=log_msg)
    return "<h1 style='color:red'>Something went wrong!</h1>:" + str(request.base_url)


@app.errorhandler(404)
def not_found(ex):
    """Handle 404 errors."""
    code = getattr(ex, "code", 500)
    error_name = getattr(ex, "name", "Internal Server Error")

    # return render_template("./error404.html"), 404
    app_logger.info(
        "path: %s | method: %s | code: %s | error: %s",
        request.path,
        request.method,
        code,
        error_name,
    )
    return "<h1 style='color:red'>Not found!</h1>:" + str(request.base_url)


@app.errorhandler(405)
def error_405(_):
    return "405: Not Allowed", 405


@app.route("/error")
def error(ex):
    """
    Renders the error page.

    """
    app_logger.info(
        "path: %s | method: %s | code: %s | error: %s", request.path, request.method, ex
    )
    return "<h1 style='color:red'>Error Occurred!</h1>:"


@app.route("/rest")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/rest/contact-us-mail", methods=["POST"])
@cross_origin(supports_credentials=True)
def contact_us_mail():
    data = request.json
    response = {}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
