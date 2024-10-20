import json
from logging import config, getLogger, Formatter, LogRecord, INFO, DEBUG
from logging.handlers import RotatingFileHandler

class OneLineFormatter(Formatter):
    def format(self, record: LogRecord) -> str:
        return super().format(record).replace('\n', '\\n')

def get_py_logger():
    fmt = '%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s] %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = OneLineFormatter(fmt, datefmt)

    handler = RotatingFileHandler('./log/py_logger.log', maxBytes=1000000, backupCount=3)
    handler.setFormatter(formatter)

    logger = getLogger('py_logger')
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    return logger

def get_ini_logger():
    config.fileConfig('./logging.ini')
    logger = getLogger('ini_logger')

    return logger

def get_json_logger():
    with open('./logging.json', 'r') as f:
        config.dictConfig(json.load(f))
    logger = getLogger('json_logger')

    return logger

if __name__ == '__main__':
    py_logger = get_py_logger()

    ini_logger = get_ini_logger()
    
    json_logger = get_json_logger()

    for _ in range(10000):
        py_logger.info('from py_logger')
        ini_logger.info('from ini_logger')
        json_logger.info('from json_logger')
