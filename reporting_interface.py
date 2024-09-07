from time import sleep


def present(*args, **kwargs):
    print(*args, **kwargs)
    sleep(2)
