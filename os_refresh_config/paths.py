import platform

if platform.system() == "Windows":
	from os_refresh_config.paths_windows import *
else:
	from os_refresh_config.paths_nix import *