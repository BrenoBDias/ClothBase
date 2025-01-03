FROM docker.io/python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=192.168.15.14:0.0

COPY . .

CMD [ "python", "main.py"]
