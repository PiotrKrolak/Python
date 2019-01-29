#https://docs.python.org/3/library/logging.html
# LogRecord attributes - w dokumentacji powyzej

import logging
import math

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

logging.basicConfig(filename = "quadratic_formula.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w') # filemode = 'w' - nie beda nadpisywac sie dane w pliku loga
                                                                                                          # level = logging.Loging_Level - w zależnosci jaki bedzie logging level pokarze tylko te o wartosci rownej badz wiekszej zadeklarowanej w tym miejscu

logger = logging.getLogger()

# Wykorzystanie


# Funkcja testowa
def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c = 0"""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    #Compute the discriminant - delta
    logger.debug("# Computee the discriminant - delta")
    disc = b**2 - 4 * a * c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b -math.sqrt(disc)) / (2 * a)

    # Return the roots as tuple
    logger.debug("# Return the roots")
    return(root1, root2)

# Wywolanie
roots = quadratic_formula(1, 0, -4)
print(roots)
