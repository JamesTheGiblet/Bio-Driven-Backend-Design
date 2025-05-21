"""
cell_template.py

Represents a modular service (Cell / Organ) that handles specific business logic.
It interacts with DNA principles and communicates via the Event Bus.
"""

import dna_principles # Accessing core rules
from event_bus import EventBus

class GreetingCell:
    def __init__(self, cell_id: str, event_bus: EventBus):
        self.cell_id = cell_id
        self.event_bus = event_bus
        print(f"GreetingCell '{self.cell_id}' initialized.")

    def generate_greeting(self, name: str):
        """Generates a greeting using DNA principles and publishes an event."""
        print(f"\nGreetingCell '{self.cell_id}': Tasked to greet '{name}'.")

        # Use the greeting format from DNA principles
        greeting_message = dna_principles.GREETING_FORMAT.format(name=name)
        print(f"GreetingCell '{self.cell_id}': Generated greeting: '{greeting_message}'")

        # Publish a completion event
        event_data = {"cell_id": self.cell_id, "recipient_name": name, "greeting": greeting_message}
        self.event_bus.publish("greeting.complete", event_data)
        return greeting_message
