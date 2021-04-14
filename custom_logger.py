# Logging Levels:

# 0. Notset - 0
# 1. Debug - 10
# 2. Info - 20
# 3. Warning - 30
# 4. Error  - 40
# 5. Critical - 50


import logging

# Creating and configuring the logger

log_format = "%(asctime)s - %(levelname)s - %(message)s" #determing the format we want of the log

logging.basicConfig(filename = "/file_location/filename.txt", / # use basicConfig method to set the basic configuration for logging (https://docs.python.org/3/library/logging.html#logging.basicConfig)
								level = logging.DEBUG, / # default logger level in basicConfig is 30, update it to Debug to see all messages from 1 to 5
								format = log_format, /
								filemode = 'w') # the log file is created in append mode by default, to rewrite the log-file each time, change filemode to w

logger = logging.getLogger() # create logger using getLogger method

# Tip: print(logger.level) - this command checks your logger level

#test messages

logger.debug("Debug message")

logger.info("Info message")

logger.warning("Warning message")

logger.error("Error message")

logger.critical("Critical message")

 

# to use this logging file with the program, import it and start using the logger, e.g. logger.info(#The tables have joined)