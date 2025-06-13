#!/usr/bin/python3

from flask import Flask, render_template
import os, yaml

app = Flask(__name__)
USER = os.environ['USER']
PAGES = ["config", "strugglebus"]

@app.route("/")
def home():
    return render_template('base.html', user=USER, pages=PAGES)

@app.route("/strugglebus")
def strugglebus():
    env_var = dict(os.environ)
    return render_template('struggle.html', user=USER ,envvar=env_var, pages=PAGES)

@app.route("/config")
def environ():
    data = load_config_file()
    host = os.getenv("FLASKAPP_HOSTNAME", data["hostname"])
    port = os.getenv("FLASKAPP_PORT", data["port"])
    datacenter = os.getenv("FLASKAPP_DATACENTER", data["datacenter"])
    return render_template('environ.html', host=host, port=port, datacenter=datacenter, pages=PAGES)

def load_config_file():
    with open('config.yaml', 'r', newline='') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as ymlexcp:
            print(ymlexcp)


#FLASKAPP_HOSTNAME
#FLASKAPP_PORT
#FLASKAPP_DATACENTER

