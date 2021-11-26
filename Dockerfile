FROM golang:1.16
WORKDIR /
ENV GOPATH /home/gowork
RUN go install github.com/square/certigo@latest
RUN ls -l $GOPATH/bin

FROM python:3.9
# Set the working directory
WORKDIR /home/dynamic-certigo
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# Set GOPATH as PATH
ENV PATH=$GOPATH/bin:$PATH
RUN ls -l $GOPATH/bin
RUN certigo --version
# Copy all the files
COPY . .
RUN chown -R root:root .
# Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt
# Expose the required port
EXPOSE 8080
# Run the command
CMD ["gunicorn", "wsgi:app"]