import logging

def setup_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    # File handler
    fh = logging.FileHandler("bot.log")
    fh.setLevel(logging.INFO)
    
    # Console handler (for Rich output we can override later)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

logger = setup_logger()
