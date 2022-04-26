"""
Main module of the server file
"""

from flask import render_template

import config


connex_app = config.connex_app

connex_app.add_api("swagger.yml")

@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")

if __name__ == "__main__":
    connex_app.run(host='127.0.0.1',port=5000,debug=True)