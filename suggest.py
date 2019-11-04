# from https://dev.to/apcelent/deploying-flask-on-aws-lambda-4k42
from flask import Flask, jsonify, request
from itertools import permutations
from spellchecker import SpellChecker
import json


#print('\n'.join( sorted(known) ))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})

@app.route('/suggest/')
def suggest_strings():
    ss = request.args.get('letters', default='hello')
    perms = []

    for l in range(3, len(ss)+1):
        print(l)
        perm = permutations( list(ss), l)
        for i in perm:
            w = ''.join(i)
            perms.append(w)

    spell = SpellChecker( distance=1 )
    w = list(spell.known( perms ))
    resultm = {"letters": ss ,"words" : w}
    returnjson.dumps(resultm)

if __name__ == '__main__':
 app.run()
