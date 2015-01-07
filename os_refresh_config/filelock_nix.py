import fcntl
import os

LOCK_EX = fcntl.LOCK_EX
LOCK_SH = fcntl.LOCK_SH
LOCK_NB = fcntl.LOCK_NB

def lock(file, flags):
    try:
        fcntl.flock(file.fileno(), flags)
    except IOError, exc_value:
        #  IOError: [Errno 11] Resource temporarily unavailable
        if exc_value[0] == 11:
            raise LockException(LockException.LOCK_FAILED, exc_value[1])
        else:
            raise

def unlock(file):
    fcntl.flock(file.fileno(), fcntl.LOCK_UN)