# wordsuggest
suggest dictionary words based on given set of letters

build

    pyenv venv
    source venv/bin/activate
    pip install -r requirements.txt

local run

    FLASK_APP=suggest.py  flask run

    curl -s http://127.0.0.1:5000/suggest/?letters="bob" | jq -r .words[]


remote deploy w zappa

    zappa init
    zappa deploy dev

    curl -s <api endpoint>
