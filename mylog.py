import logging,sys

def setup_logger(logName):
    logger = logging.getLogger(logName)  # default logger
    logger.setLevel(logging.DEBUG)

    # Create file handler
    fh = logging.FileHandler('mylog.txt')
    fmt = '%(asctime)s - [%(levelname)s] - %(name)s - %(message)s (%(lineno)d)'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)

    return logger
    
if __name__ == "__main__":
    logger = setup_logger(logName='alexzhang')
    logger.info("Testing logger")