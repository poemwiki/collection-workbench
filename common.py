import time


class BatchIterator:
    def __init__(self, threshold: int, process, duration: int = 0) -> None:
        self.threashold = threshold
        self.process = process
        self.bucket = []
        self.duration = duration

    def iterate(self, one):
        self.bucket.append(one)
        if len(self.bucket) == self.threashold:
            self.process(self.bucket)
            self.bucket.clear()
            if self.duration:
                time.sleep(self.duration)

    def tail(self):
        self.process(self.bucket)
