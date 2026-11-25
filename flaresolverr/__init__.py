<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 63edbdf (Expose resolver functions to python package)
=======
>>>>>>> beba0b3 (feat(logger): use custom logger on flaresolverr)
"""FlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection."""

from .flaresolverr import init, start_webserver
from .utils import get_chrome_exe_path
from .dtos import V1RequestBase, ChallengeResolutionT
from .flaresolverr_service import resolve_challenge
<<<<<<< HEAD
<<<<<<< HEAD
from .exceptions import FlaresolverrException

__version__ = "3.5.2"

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
>>>>>>> 8bb5e29 (Proper python packaging with Hatch)
=======
=======
from .exceptions import FlaresolverrException
>>>>>>> 5d38858 (refactor: replace generic exceptions with FlaresolverrException for better error handling)

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
<<<<<<< HEAD
>>>>>>> 63edbdf (Expose resolver functions to python package)
=======
=======
__version__ = "3.4.3"
>>>>>>> 75c7dc1 (Proper python packaging with Hatch)
>>>>>>> beba0b3 (feat(logger): use custom logger on flaresolverr)
