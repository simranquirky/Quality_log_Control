import logging
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, log_paths):
        self.log_paths = log_paths
        self.loggers = self.setup_loggers()

    def setup_loggers(self):
        loggers = {}
        for path in self.log_paths:
            logger = logging.getLogger(path)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler(path)
            handler.setFormatter(logging.Formatter('%(message)s'))
            logger.addHandler(handler)
            loggers[path] = logger
        return loggers

    def ingest_log(self, log_data):
        try:
            file_path = log_data['metadata']['source']
            logger = self.loggers[file_path]
            log_string = json.dumps(log_data)
            logger.info(log_string)
        except Exception as e:
            print(f"Error ingesting log: {e}")

