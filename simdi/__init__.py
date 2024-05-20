import heapq
import time

class Event:
    def __init__(self, timestamp, event_type, data):
        self.timestamp = timestamp
        self.event_type = event_type
        self.data = data

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class SimulationEngine:
    def __init__(self):
        self.event_queue = []
        self.current_time = 0

    def schedule_event(self, event):
        heapq.heappush(self.event_queue, event)

    def run(self):
        while self.event_queue:
            event = heapq.heappop(self.event_queue)
            self.current_time = event.timestamp
            self.process_event(event)

    def process_event(self, event):
        print(f"Processing event: {event.event_type} at {event.timestamp}")
      
if __name__ == "__main__":
    engine = SimulationEngine()
    engine.schedule_event(Event(time.time(), "START", {}))
    engine.run()
