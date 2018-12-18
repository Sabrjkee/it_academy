import os


def ping(hostname:str):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        pingstatus = True
    else:
        pingstatus = False

    return pingstatus