from multiprocessing import cpu_count



# Socket Path

bind = 'unix:/home/ubuntu/api/HackathonBBVA2022/gunicorn.sock'



# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/home/ubuntu/api/HackathonBBVA2022/access_log'

errorlog =  '/home/ubuntu/api/HackathonBBVA2022/error_log'