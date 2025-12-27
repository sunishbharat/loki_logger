## loki_logger
Generic logger to support Grafana Loki logging using standard python logging interface.

## Usage
```python

from loki_logger.core import loki_logger

logger = loki_logger(level=logging.DEBUG, tags={"app": "fastapi", "env":"block"})

logger.info("Info: 1.User logged in", extra={"user_id": 123})
logger.debug("Debug: 2.Debug info")
log_dict = {
    "warn":"Memory full",
    "Cpu": "99%"
}
logger.critical(log_dict)
```
### Grafana Loki logs.
From localhost: http://localhost:3000/

<img width="1500" height="547" alt="image" src="https://github.com/user-attachments/assets/371e9323-158c-4f2d-aedb-eab29d57188a" />

### Grafana Loki installation link
https://grafana.com/docs/loki/latest/setup/install/
