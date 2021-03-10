FROM python:3-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY suggest.py .

EXPOSE 5000

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

#     FLASK_APP=suggest.py  flask run
ENV FLASK_APP=suggest.py
CMD [ "flask", "run" ]
CMD [ "python", "suggest.py", "runserver", "-h", "0.0.0.0" ]
