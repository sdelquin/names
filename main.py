from flask import Flask, send_from_directory
import glob
import re
import json
import os
import random

app = Flask(__name__)
app.debug = False

my_path = os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def get_list():
    r = []
    files = glob.glob("files/*.names")
    for f in files:
        r.append(re.match(r"^.*/(.*)\.names", f).group(1))
    return json.dumps(r)


@app.route("/<universe>/")
def get_universe(universe):
    try:
        with open("{}/files/{}.names".format(my_path, universe)) as f:
            return json.dumps([l.strip() for l in f.readlines()])
    except FileNotFoundError:
        return "ERROR"


@app.route("/<universe>/random/")
def get_randomized(universe):
    try:
        with open("{}/files/{}.names".format(my_path, universe)) as f:
            return random.choice(f.readlines()).strip()
    except FileNotFoundError:
        return "ERROR"


@app.route("/random/")
def get_global_randomized():
    universes = json.loads(get_list())
    return get_randomized(random.choice(universes))


# management of well-known for LetsEncrypt
@app.route("/.well-known/<path:path>")
def well_known(path):
    pwd = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(pwd, ".well-known"), path)


if __name__ == "__main__":
    app.debug = True
    app.run()
