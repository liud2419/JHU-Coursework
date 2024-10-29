import threading

class Fork:
    def __init__(self):
        self.lock = threading.Lock()
    def acquire_fork(self):
        return self.lock.acquire(blocking=False)
    def release_fork(self):
        self.lock.release()