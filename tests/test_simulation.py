from simdi.simulation.event import Event
from simdi.simulation.simulation_engine import SimulationEngine

def test_event_order():
    engine = SimulationEngine()
    
    events_executed = []

    def action1():
        events_executed.append("event1")

    def action2():
        events_executed.append("event2")

    def action3():
        events_executed.append("event3")

    engine.schedule_event(Event(10, action1))
    engine.schedule_event(Event(5, action2))
    engine.schedule_event(Event(15, action3))

    engine.run()

    assert events_executed == ["event2", "event1", "event3"]

def test_empty_queue():
    engine = SimulationEngine()
    assert engine.event_queue.is_empty()
