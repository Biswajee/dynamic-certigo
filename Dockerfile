FROM golang:1.16
WORKDIR /
RUN go install github.com/square/certigo@latest

FROM python:3.9
# Set the working directory
WORKDIR /home/dynamic-certigo
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# Copy all the files
COPY . .
RUN chown -R root:root .
# Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
# Expose the required port
EXPOSE 8080
# Run the command
CMD gunicorn -w 4 -b 0.0.0.0:8080 wsgi:app --daemon