from mongoengine import connect

from monkey_island.cc.environment.environment import env

# This section sets up the DB connection according to the environment.
#   If testing, use mongomock which only emulates mongo. for more information, see
#   http://docs.mongoengine.org/guide/mongomock.html .
#   Otherwise, use an actual mongod instance with connection parameters supplied by env.
if env.testing:  # See monkey_island.cc.environment.testing
    connect('mongoenginetest', host='mongomock://localhost')
else:
    connect(db=env.mongo_db_name, host=env.mongo_db_host, port=env.mongo_db_port)

# Order of importing matters here, for registering the embedded and referenced documents before using them.
from .config import Config  # noqa: F401
from .creds import Creds  # noqa: F401
from .monkey_ttl import MonkeyTtl  # noqa: F401
from .pba_results import PbaResults  # noqa: F401
from .command_control_channel import CommandControlChannel  # noqa: F401
from .monkey import Monkey  # noqa: F401
