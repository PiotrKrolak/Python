#https://docs.python.org/3/library/logging.html
# LogRecord attributes - w dokumentacji powyzej

import logging

# print(dir(logging))

################
# Loging Levels:
# NOTSET = 0
# DEBUG = 10
# INFO = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50
###############


# Stworzenie i konfiguracja loggera
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logging.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w') # filemode = 'w' - nie beda nadpisywac sie dane w pliku loga
                                                                                                          # level = logging.Loging_Level - w zależnosci jaki bedzie logging level pokarze tylko te o wartosci rownej badz wiekszej zadeklarowanej w tym miejscu

logger = logging.getLogger()

# Test messages
logger.debug("Message with DEBUG loging level")
logger.info("Message with INFO loging level")
logger.warning("Message with WARNING loging level")
logger.error("Message with ERROR loging level")
logger.critical("Message with CRITICAL loging level")
