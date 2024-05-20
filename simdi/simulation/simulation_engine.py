from .event_queue import EventQueue

class SimulationEngine:
    def __init__(self):
        self.event_queue = EventQueue()
        self.current_time = 0

    def schedule_event(self, event):
        self.event_queue.push(event)

    def run(self):
        while not self.event_queue.is_empty():
            event = self.event_queue.pop()
            self.current_time = event.time
            event.action()
