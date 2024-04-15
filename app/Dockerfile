FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=192.168.15.14:0.0

COPY . .

CMD [ "python", "app.py"]


