FROM python:3

RUN pip install requests

WORKDIR /app
COPY decrypt-demystyfy.py .

EXPOSE 8080
CMD [ "python3", "./decrypt-demystyfy.py" ]
