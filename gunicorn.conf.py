import multiprocessing
from os import environ

port = environ.get('PORT')
if port is None:
    bind = "0.0.0.0:8080"
else:
    bind = f"0.0.0.0:{port}"
workers = multiprocessing.cpu_count() * 2 + 1
