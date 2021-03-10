FROM python:3-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY suggest.py .

#     FLASK_APP=suggest.py  flask run
ENV FLASK_APP=suggest.py
CMD [ "flask", "run" ]
