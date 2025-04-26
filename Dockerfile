FROM ubuntu:latest


WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m venv venv 
RUN source venv/bin/activate
RUN venv/bin/pip install --no-cache-dir -r requirements.txt
CMD ["venv/bin/python", "bot.py"] 