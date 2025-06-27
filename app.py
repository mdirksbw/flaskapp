#!/usr/bin/python3

from flask import Flask, render_template
import os, yaml

app_name = os.getenv('APP_NAME', "flaskapp")
USER = os.environ['USER']
PAGES = ["config", "strugglebus"]

app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template('views/home.html', user=USER, pages=get_pages(), APP_NAME=app_name)

@app.route("/strugglebus")
def strugglebus():
    env_var = dict(os.environ)
    return render_template('views/strugglebus.html', user=USER, pages=get_pages(), APP_NAME=app_name, envvar=env_var)

@app.route("/config")
def config():
    data = load_config_file()
    host = os.getenv("FLASKAPP_HOSTNAME", data["hostname"])
    port = os.getenv("FLASKAPP_PORT", data["port"])
    datacenter = os.getenv("FLASKAPP_DATACENTER", data["datacenter"])
    return render_template('views/config.html', host=host, port=port, datacenter=datacenter, pages=get_pages(), APP_NAME=app_name, user=USER)

def load_config_file():
    with open('config.yaml', 'r', newline='') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as ymlexcp:
            print(ymlexcp)

def get_pages():
    pages = list(app.view_functions.keys())
    pages.remove("static")
    return pages

#FLASKAPP_HOSTNAME
#FLASKAPP_PORT
#FLASKAPP_DATACENTER

