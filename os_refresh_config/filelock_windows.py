"""
Windows specific file locking. This requires pywin32
Most of this module has been taken from:
	http://code.activestate.com/recipes/65203/
"""

import win32con
import win32file
import pywintypes

LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
LOCK_SH = 0 # the default
LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
__overlapped = pywintypes.OVERLAPPED()

def lock(file, flags):
    hfile = win32file._get_osfhandle(file.fileno())
    try:
        win32file.LockFileEx(hfile, flags, 0, -0x10000, __overlapped)
    except pywintypes.error, exc_value:
        # error: (33, 'LockFileEx', 'The process cannot access the file because another process has locked a portion of the file.')
        if exc_value[0] == 33:
            raise LockException(LockException.LOCK_FAILED, exc_value[2])
        else:
            # Q:  Are there exceptions/codes we should be dealing with here?
            raise

def unlock(file):
    hfile = win32file._get_osfhandle(file.fileno())
    try:
        win32file.UnlockFileEx(hfile, 0, -0x10000, __overlapped)
    except pywintypes.error, exc_value:
        if exc_value[0] == 158:
            # error: (158, 'UnlockFileEx', 'The segment is already unlocked.')
            # To match the 'posix' implementation, silently ignore this error
            pass
        else:
            # Q:  Are there exceptions/codes we should be dealing with here?
            raise