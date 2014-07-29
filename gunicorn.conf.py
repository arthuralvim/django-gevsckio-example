from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count() + 1

bind = '0.0.0.0:8000'
max_requests = 10000
worker_class = 'gevent'
workers = max_workers()
