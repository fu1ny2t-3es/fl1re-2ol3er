<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cd5906 (Expose resolver functions to python package)
=======
>>>>>>> 447c45a (feat(logger): use custom logger on flaresolverr)
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
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 1117914 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> bbad2ee (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 8ad60c3 (feat(logger): use custom logger on flaresolverr)
=======
=======
=======
=======
>>>>>>> 3cd5906 (Expose resolver functions to python package)
<<<<<<< HEAD
>>>>>>> 2a92c69 (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> 93ba1ba (feat(logger): use custom logger on flaresolverr)
<<<<<<< HEAD
>>>>>>> f1b5a89 (feat(logger): use custom logger on flaresolverr)
=======
=======
=======
=======
=======
__version__ = "3.4.3"
>>>>>>> c56d9e0 (Proper python packaging with Hatch)
>>>>>>> 447c45a (feat(logger): use custom logger on flaresolverr)
>>>>>>> a5ed274 (feat(logger): use custom logger on flaresolverr)
>>>>>>> e3f1dac (feat(logger): use custom logger on flaresolverr)
>>>>>>> b672573 (feat(logger): use custom logger on flaresolverr)
