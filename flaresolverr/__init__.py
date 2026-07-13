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
>>>>>>> ad32d26 (feat(logger): use custom logger on flaresolverr)
=======
=======
>>>>>>> 8ad60c3 (feat(logger): use custom logger on flaresolverr)
>>>>>>> f848326 (Proper python packaging with Hatch)
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
>>>>>>> fd898f7 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> d32dff0 (feat(logger): use custom logger on flaresolverr)
=======
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
=======
>>>>>>> 633f8aa (Proper python packaging with Hatch)
>>>>>>> 1117914 (feat(logger): use custom logger on flaresolverr)
>>>>>>> bbad2ee (feat(logger): use custom logger on flaresolverr)
>>>>>>> 8ad60c3 (feat(logger): use custom logger on flaresolverr)
