class Event:
    def __init__(self, time, action):
        self.time = time
        self.action = action

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f"Event(time={self.time}, action={self.action})"
