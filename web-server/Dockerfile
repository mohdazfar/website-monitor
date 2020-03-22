FROM python:3.5-slim
MAINTAINER muhammad.faizan@sanoma.com
USER root
WORKDIR /app
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
