"""
main.py

Main entry point for the biosim BDBD system.
Demonstrates initialization and basic interaction of components.
This script is intended to be run from the root of the 'biosim' directory.
"""
from dna import principles
from event_system.bus import EventBus
from cells.generic_cell import GenericCell # Assuming you have a GenericCell in cells/
from cortex.orchestrator import CortexOrchestrator

def run_system_demo():
    print(f"--- Starting BDBD System Demo for: {principles.SYSTEM_NAME} v{principles.SYSTEM_VERSION} ---")

    # 1. Initialize core infrastructure: The Event Bus
    event_bus = EventBus()

    # 2. Initialize the Cortex (Orchestrator)
    # The Cortex is the central intelligence, coordinating cells and reacting to events.
    cortex = CortexOrchestrator(event_bus=event_bus)

    # 3. Create and register Cells (modular components)
    # Cells are the workhorses, performing specific tasks.
    cell1_id = "data_processor_alpha"
    cell1 = GenericCell(cell_id=cell1_id, event_bus=event_bus)
    cortex.register_cell(cell1)

    # Example: Create another cell
    cell2_id = "notifier_beta"
    cell2 = GenericCell(cell_id=cell2_id, event_bus=event_bus) # Using GenericCell for demo
    cortex.register_cell(cell2)


    # 4. Subscribe Cortex (or other components) to relevant events
    # This allows for reactive, event-driven behavior.
    # Event types are now more specific, like "{cell_id}.{action}.complete"
    # Cortex now has specific handlers for different types of completions.
    event_bus.subscribe(f"{cell1_id}.analyze_data.complete", cortex.handle_data_analysis_complete)
    event_bus.subscribe(f"{cell2_id}.send_notification.complete", cortex.handle_notification_sent)
    # You could also have cells subscribe to each other's events if needed.


    # 5. Cortex orchestrates tasks
    # The Cortex delegates work to the appropriate cells.
    print(f"\nMain: Attempting to delegate 'analyze_data' task to {cell1_id}.")
    task1_payload = {"action": "analyze_data", "source_id": "sensor_A01", "data_points": [1,2,3,4,5]}
    # The main script just initiates the first task. Chaining happens inside the Cortex.
    cortex.delegate_task_to_cell(cell1_id, task1_payload)
    # Add more complex interactions, error handling, or AI-driven adaptations here as the system evolves.

    print(f"\n--- BDBD System Demo for: {principles.SYSTEM_NAME} Finished ---")

if __name__ == "__main__":
    run_system_demo()
