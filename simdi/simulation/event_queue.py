import heapq

class EventQueue:
    def __init__(self):
        self._queue = []

    def push(self, event):
        heapq.heappush(self._queue, event)

    def pop(self):
        return heapq.heappop(self._queue) if self._queue else None

    def is_empty(self):
        return len(self._queue) == 0
