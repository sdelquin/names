from flask import Flask
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
    except:
        return "ERROR"


@app.route("/<universe>/random/")
def get_randomized(universe):
    try:
        with open("{}/files/{}.names".format(my_path, universe)) as f:
            return random.choice(f.readlines()).strip()
    except:
        return "ERROR"


@app.route("/random/")
def get_global_randomized():
    universes = json.loads(get_list())
    return get_randomized(random.choice(universes))


if __name__ == "__main__":
    app.debug = True
    app.run()
