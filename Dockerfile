FROM python:3.9.5-alpine3.13

WORKDIR . 

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]
