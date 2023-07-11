import logging


def app_logger():
    logging.basicConfig(
        filename="coderogres.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    return logging.getLogger("coderogres.log")
