# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install pandas scikit-learn joblib flask

EXPOSE 8000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]


# git config --global user.name "ohmfordev"
# git config --global user.email "sittiporn.emr@gmail.com"