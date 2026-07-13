<<<<<<< HEAD
"""FlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection."""

from .flaresolverr import init, start_webserver
from .utils import get_chrome_exe_path
from .dtos import V1RequestBase, ChallengeResolutionT
from .flaresolverr_service import resolve_challenge
from .exceptions import FlaresolverrException

__version__ = "3.4.3"

__all__ = [
    "init",
    "start_webserver",
    "get_chrome_exe_path",
    "V1RequestBase",
    "ChallengeResolutionT",
    "resolve_challenge",
    "FlaresolverrException",
]
=======
__version__ = "3.4.3"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 75c7dc1 (Proper python packaging with Hatch)
=======
>>>>>>> f848326 (Proper python packaging with Hatch)
>>>>>>> 2a9e5c0 (feat(logger): use custom logger on flaresolverr)
=======
=======
>>>>>>> 1a4d7a4 (feat(logger): use custom logger on flaresolverr)
>>>>>>> f848326 (Proper python packaging with Hatch)
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
>>>>>>> 11e979d (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 330290d (feat(logger): use custom logger on flaresolverr)
=======
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
=======
>>>>>>> 633f8aa (Proper python packaging with Hatch)
>>>>>>> 5557d20 (feat(logger): use custom logger on flaresolverr)
>>>>>>> 5f4d7e8 (feat(logger): use custom logger on flaresolverr)
>>>>>>> 1a4d7a4 (feat(logger): use custom logger on flaresolverr)
