from pasport_mo import celery_app

import os


@celery_app.task
def ping(hostname: str):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        return True
    else:
        return False
