# from https://dev.to/apcelent/deploying-flask-on-aws-lambda-4k42
from flask import Flask, jsonify, request
from itertools import permutations
from spellchecker import SpellChecker
import json


app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({"message": "Hello World!"})

@app.route('/info/')
def info():
    return jsonify({"message": "info: TBD"})

@app.route('/health/')
def health():
    return jsonify({"message": "health: TBD"})

@app.route('/suggest/')
def suggest():
    ss = request.args.get('letters', default='hello')
    perms = []

    for l in range(3, len(ss)+1):
        #print(l)
        perm = permutations( list(ss), l)
        for i in perm:
            w = ''.join(i)
            perms.append(w)

    spell = SpellChecker( distance=1 )
    k = spell.known( perms )
    w = sorted(list(k))
    rmap = {"letters": ss ,"words" : w}
    jd = json.dumps(rmap)
    print(jd)
    return jd

if __name__ == '__main__':
 app.run()
