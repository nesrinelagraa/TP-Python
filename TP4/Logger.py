import logging

class Logger():
    def __init__(self, file='example.log'):
        logging.basicConfig(filename=file,format='%(asctime)s %(message)s')

    def infolog(self, message):
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.warning(message)