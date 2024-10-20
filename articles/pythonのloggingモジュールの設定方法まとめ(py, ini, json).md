# 概要
pythonのloggingモジュールを使うと`print()`よりも詳細なログ出力ができる。
タイムスタンプを付加できたり、ログファイルを出力できたりいろいろと嬉しいことがある。
loggingの設定方法がいくつかあるのでまとめる。

# .pyファイル
loggingモジュールをインポートしてそのまま定義する方法。
エディタのコード補完が効くので個人的にはこの方法が好き。
```py
from logging import getLogger, Formatter, DEBUG
from logging.handlers import RotatingFileHandler

# フォーマット
fmt = '%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s] %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = Formatter(fmt, datefmt)

# ハンドラ
handler = RotatingFileHandler('./log/py_logger.log', maxBytes=1000000, backupCount=3)
handler.setFormatter(formatter)

# ロガー定義
logger = getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(handler)
```

# .iniファイル
`logging.config.fileConfig()`を使って.iniファイルを読み込む方法。
```py
from logging import config, getLogger

config.fileConfig('./logging.ini')
logger = getLogger('ini_logger') # 適宜変更する。
```
```ini
[loggers]
keys=root,ini_logger

[handlers]
keys=fileHandler

[formatters]
keys=fileFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_ini_logger]
level=DEBUG
handlers=fileHandler
qualname=ini_logger
propagate=0

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=INFO
formatter=fileFormatter
args=('./log/ini_logger.log', 'a', 1000000, 3)

[formatter_fileFormatter]
format=%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s] %(message)s
datefmt=%Y-%m-%d %H:%M:%S

```

# .jsonファイル
`logging.config.dictConfig()`を使って.jsonファイルを読み込む方法。
```py
import json
from logging import config, getLogger

with open('./logging.json', 'r') as f:
    config.dictConfig(json.load(f))
logger = getLogger('json_logger') # 適宜変更する。
```
```json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "fileFormatter": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },

    "handlers": {
        "fileHandler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "fileFormatter",
            "filename": "./log/json_logger.log",
            "maxBytes": 1000000,
            "backupCount": 3
        }
    },

    "loggers": {
        "json_logger": {
            "level": "DEBUG",
            "handlers": ["fileHandler"],
            "propagate": false
        }
    },

    "root": {
        "level": "INFO"
    }
}
```
