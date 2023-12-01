FROM python:3.13.0a2-alpine3.18

LABEL maintainer="Merhan Motmaen <motmaen73@gmail.com>"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENV APP_NAME=StringMatcherApp

# Run tests when the container launches
CMD ["python", "-m", "unittest", "tests/test.py"]
