<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 63edbdf (Expose resolver functions to python package)
=======
>>>>>>> 4dcf676 (feat(logger): use custom logger on flaresolverr)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4dcf676 (feat(logger): use custom logger on flaresolverr)
=======
=======
>>>>>>> 1b8924d (feat(logger): use custom logger on flaresolverr)
=======
>>>>>>> 9c035e0 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 75c7dc1 (Proper python packaging with Hatch)
=======
>>>>>>> f848326 (Proper python packaging with Hatch)
>>>>>>> ad32d26 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 8ee9d7f (feat(logger): use custom logger on flaresolverr)
=======
=======
=======
>>>>>>> 8ad60c3 (feat(logger): use custom logger on flaresolverr)
>>>>>>> f848326 (Proper python packaging with Hatch)
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
>>>>>>> fd898f7 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> d32dff0 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 1b8924d (feat(logger): use custom logger on flaresolverr)
=======
=======
=======
>>>>>>> 4738da8 (Proper python packaging with Hatch)
=======
>>>>>>> 633f8aa (Proper python packaging with Hatch)
>>>>>>> 1117914 (feat(logger): use custom logger on flaresolverr)
>>>>>>> bbad2ee (feat(logger): use custom logger on flaresolverr)
>>>>>>> 8ad60c3 (feat(logger): use custom logger on flaresolverr)
>>>>>>> 9c035e0 (feat(logger): use custom logger on flaresolverr)
