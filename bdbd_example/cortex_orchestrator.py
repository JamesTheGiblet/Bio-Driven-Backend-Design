"""
cortex_orchestrator.py

Represents a simplified Cerebral Cortex (AI layer for behavior adjustment & control).
It orchestrates Cells, subscribes to events, and makes decisions.
"""

from event_bus import EventBus
from cell_template import GreetingCell # Changed from ProcessingCell
import dna_principles # Accessing core rules

class CortexOrchestrator:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.cells = {}
        print("CortexOrchestrator (Cerebral Cortex) initialized.")

        # Cortex subscribes to events to monitor and react
        self.event_bus.subscribe("greeting.complete", self.handle_greeting_complete_event)

    def register_cell(self, cell: GreetingCell): # Changed type hint
        """Registers a cell with the orchestrator."""
        self.cells[cell.cell_id] = cell
        print(f"Cortex: Registered GreetingCell '{cell.cell_id}'")

    def initiate_greeting(self, cell_id: str, name_to_greet: str):
        """Instructs a specific cell to generate a greeting."""
        if cell_id in self.cells:
            print(f"\nCortex: Instructing GreetingCell '{cell_id}' to greet '{name_to_greet}'.")
            self.cells[cell_id].generate_greeting(name_to_greet)
        else:
            print(f"Cortex: Error - GreetingCell '{cell_id}' not found.")

    def handle_greeting_complete_event(self, event_data):
        """Handles events indicating a cell has finished generating a greeting."""
        print(f"Cortex: Received 'greeting.complete' event from '{event_data['cell_id']}'.")
        print(f"Cortex: Greeting for '{event_data['recipient_name']}' is: '{event_data['greeting']}'")
        print(f"Cortex: System version according to DNA: {dna_principles.SYSTEM_VERSION}")

if __name__ == "__main__":
    # Initialize the core components
    bus = EventBus()
    cortex = CortexOrchestrator(event_bus=bus)

    # Create and register some cells
    greeter_cell = GreetingCell(cell_id="Greeter-Alpha", event_bus=bus)
    cortex.register_cell(greeter_cell)

    # Cortex orchestrates some actions
    cortex.initiate_greeting("Greeter-Alpha", "World")
    cortex.initiate_greeting("Greeter-Alpha", "BDBD User")
