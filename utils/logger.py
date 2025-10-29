import logging, os

def get_logger(name:str, log_file:str=None, level:int=logging.INFO) -> logging.Logger:
    """
    Creates and returns a logger with the specified name and log file.

    Args:
        name (str): The name of the logger.
        log_file (str, optional): The file to which logs should be written. If None, logs will only be printed to console.
        level (int, optional): The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger