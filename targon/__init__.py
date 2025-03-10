import os 

from . import protocol
from . import prompts
from .updater import autoupdate

from dotenv import load_dotenv

load_dotenv()
from .miner.search import query as search
from .miner.search import QueryParams

__version__ = "0.5.3"
version_split = __version__.split(".")
__spec_version__ = (
    (1000 * int(version_split[0]))
    + (10 * int(version_split[1]))
    + (1 * int(version_split[2]))
)

__api_endpoint__ = "https://us-central-02.db.sybil.com"