FROM golang:1.16
WORKDIR /
RUN go install github.com/square/certigo

FROM python:3.9
# Set the working directory
WORKDIR /
# Copy all the files
COPY . .
# Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
# Expose the required port
EXPOSE 5000
# Run the command
CMD gunicorn main:app