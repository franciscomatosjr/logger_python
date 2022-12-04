import logging
import os

"""
    Author: Francisco Matos 
    githut: https://github.com/franciscomatosjr/logger_python.git
"""

try:
    log_nome = os.environ['NAMEDCLASS']
except:
    log_nome = __name__


logger = logging.getLogger(log_nome)

if 'LOGGER_LEVEL' in os.environ:

    LOGGER_LEVEL = os.environ['LOGGER_LEVEL']

    if LOGGER_LEVEL == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif LOGGER_LEVEL == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    elif LOGGER_LEVEL == 'WARNING':
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.INFO)

else:
    logger.setLevel(logging.INFO)


logging.basicConfig(level=logger.level, filemode="w", format="[%(levelname)s] - [%(name)s] - [%(asctime)s] - %(message)s")


def log_and_call(logger=logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if logger == 'ERROR':
                logger.error(f'Executando:  {func.__module__}.{func.__name__}')
            elif logger == 'WARNING':
                logger.warning(f'Executando:  {func.__module__}.{func.__name__}')
            elif logger == 'DEBUG':
                logger.debug(f'Executando:  {func.__module__}.{func.__name__}')
            else:
                logger.info(f'Executando:  {func.__module__}.{func.__name__}')

            return func(*args, **kwargs)
        return wrapper
    return decorator
