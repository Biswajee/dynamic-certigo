FROM python:3.9

# Set the working directory
WORKDIR /

# Copy all the files
COPY . .

# Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# Install go and certigo
RUN cd ~
RUN curl -O https://dl.google.com/go/go1.16.3.linux-amd64.tar.gz
RUN tar xvf go1.16.3.linux-amd64.tar.gz
RUN chown -R root:root ./go
RUN mv go /usr/local
RUN export GOPATH=$HOME/work
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
RUN go install github.com/square/certigo

# Expose the required port
EXPOSE 5000

# Run the command
CMD gunicorn main:app