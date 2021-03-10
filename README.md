# wordsuggest
suggest dictionary words based on given set of letters

build

    (assumed you have pyenv and pyenv virtualenv installed)`

    pyenv virtualenv wordsuggestvenv
    pyenv activate wordsuggestvenv
    pip install -r requirements.txt

local run

    FLASK_APP=suggest.py  flask run

    curl -s http://127.0.0.1:5000/suggest?letters="bob" | jq -r .words[]

    curl -s http://127.0.0.1:5000/suggest?letters="mcaeakl" | jq -r .words[]


remote deploy w zappa

    zappa init
    zappa deploy dev

    curl -s <api endpoint>


exit project

    pyenv deactivate

docker build -t suggest:latest .

docker run --rm -it suggest:latest

