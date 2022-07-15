#!/usr/bin/env python3

__version__= "0.1.0"
__author__= "Francisco Wesley"

import logging
import os
from logging import handlers

# my instance

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("log.py", logging.DEBUG)


#level / create console handler
#ch = logging.StreamHandler()  #Console/terminal/stderr
#ch.setLevel(logging.DEBUG)

fh = handlers.RotatingFileHandler("meulog.log", maxBytes=10**6, backupCount=10)
fh.setLevel(log_level)

#formatting
fmt = logging.Formatter(
    '%(asctime)s | archive: %(name)s | %(levelname)s | '
    'line: %(lineno)d | message: %(message)s'
)
fh.setFormatter(fmt)
#send log for console handler
log.addHandler(fh)

'''
log.debug("Mensagem para o time técnico")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral ex:banco de dados")
'''

try:
    1/0
except ZeroDivisionError as e:
    log.error("%s",str(e))