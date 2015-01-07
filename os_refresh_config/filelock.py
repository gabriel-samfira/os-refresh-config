import platform


if platform.system() == "Windows":
	from os_refresh_config.filelock_windows import *
else:
	from os_refresh_config.filelock_nix import *


class LockException(Exception):
    # Error codes:
    LOCK_FAILED = 1

