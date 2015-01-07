import os

TMPDIR = os.environ.get("TEMP", "C:\\")
DEFAULT_LOCK_FILE = os.path.join(TMPDIR, "os-refresh-config.lock")

DEFAULT_BASE_DIR = 'C:\\tripleo\\libexec\\os-refresh-config'
# For compatibillity
OLD_BASE_DIR = DEFAULT_BASE_DIR
