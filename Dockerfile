# 1 
FROM python:3.8

# 2
RUN pip install Flask flask_cors gunicorn pandas

# 3
COPY . /app
WORKDIR /app

# 4
ENV PORT 5000

# 5
# CMD exec python /app/server.py
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 server:app