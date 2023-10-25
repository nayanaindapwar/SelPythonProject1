# LoggingDemo

import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('/home/nayana/PycharmProjects/MyTestProject/pytestsDemo/logfile.log')
    formatter = logging.Formatter("%(asctime)S : %(levelname)S : %(name)S : %(message)S")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)

    logger.debug("Debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logging.error("Major error is observed")
    logging.critical("Critical issue")






