import sys, time, threading, pyfiglet, os
from libs.colors import *

class Spinner():
    busy = False
    delay = 1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False
    
class utils():
    def banner(value):
        version = '2.0.0'
        ascTime = time.asctime()
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        print('\n')
        ascii_banner=pyfiglet.figlet_format(value)
        print(W + ascii_banner)