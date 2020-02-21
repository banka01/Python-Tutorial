##

import logging
#DEBUG,INFO,ERROR,WARNING,CRITICAL

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG,filename='sample_log_file.log')

    logging.debug("In main debug")
    logging.info("in main info")
    logging.error("in main error")
    logging.warning("in warn")
    logging.critical("in crit")