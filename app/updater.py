from apscheduler.schedulers.background import BackgroundScheduler
from .schedular_update import update_something
from decouple import config



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', minutes=int(config('NEXT')))
    if config('RUN_MAIN', cast=bool):
        scheduler.start()