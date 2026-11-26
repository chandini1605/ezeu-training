import logging

# Session 28 - Application Logging

# Create logger
logger = logging.getLogger("tool_library")

# Set logging level
logger.setLevel(logging.DEBUG)

# Prevent duplicate logs
logger.propagate = False

# Define log message format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# File Handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers only once
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)