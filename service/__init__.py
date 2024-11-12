import sys
from flask import Flask
from service import config
from service.common import log_handlers

app = Flask(__name__)

app.config.from_object(config)

from service import routes, models
from service.common import error_handlers, cli_commands

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  P E T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)
except Exception as error:
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

app.logger.info("Service initialized!")
