import logging
import logging_loki
from multiprocessing import Queue
from typing import Optional, Dict, Any
import atexit


class loki_logger:
    def __init__(
            self,
            loki_url: str = "http://localhost:3100/loki/api/v1/push", 
            tags : Optional[Dict[str,str]] = None,
            version : str = "1",
            level: int = logging.INFO,
            logger_name : str = "app"
            ):
        
        self.loki_url   = loki_url
        self.tags       = tags or {"app": "fastapi", "env": "local"}
        self.version    = version
        self.level      = level
        self.logger_name= logger_name 
        self._logger    = None
        self._handler   = None
        
        self._setup_logger()
        
        atexit.register(self._cleanup)

    def _setup_logger(self):
        self.queue = Queue(-1)
        self._handler = logging.handlers.QueueHandler(self.queue)
        self.handler_loki = logging_loki.LokiHandler(
            url     = self.loki_url,
            tags    = self.tags,
            version = self.version
        )
        self._listener = logging.handlers.QueueListener(self.queue, self.handler_loki)
        self._listener.start()

        self._logger = logging.getLogger(self.logger_name)
        self._logger.setLevel(self.level)
        
        if not self._logger.handlers:
            self._logger.addHandler(self._handler)

            
    def _cleanup(self):
        if self._handler:
            self._handler.flush()
            self._listener.stop()

    @property
    def logger(self) -> logging.Logger:
        return self._logger
    
    '''
    Maintain standard logging interface
    '''
    def info(self, msg, *args, **kwargs):
        return self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return self._logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self._logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self._logger.critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        return self._logger.log(level, msg, *args, **kwargs)
    
    def exception(self, msg, *args, exc_info=True, **kwargs):
        return self._logger.exception(msg, *args, exc_info=exc_info, **kwargs)