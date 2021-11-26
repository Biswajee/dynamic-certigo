import multiprocessing
from os import environ

port = environ.get('PORT')
if port is None:
    bind = "127.0.0.1:8080"
else:
    bind = f"127.0.0.1:{port}"
workers = multiprocessing.cpu_count() * 2 + 1
