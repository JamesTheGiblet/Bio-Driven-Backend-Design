"""
generic_cell.py

A template for a modular service (Cell / Organ) in biosim.
It handles specific business logic, interacts with DNA principles,
and communicates via the Event Bus.
"""

# from dna import principles # Import if this cell needs direct access to DNA
# from event_system.bus import EventBus # For type hinting if you use it

class GenericCell:
    def __init__(self, cell_id: str, event_bus): # Consider adding type hint: event_bus: EventBus
        self.cell_id = cell_id
        self.event_bus = event_bus
        print(f"GenericCell '{self.cell_id}' initialized.")

    def perform_task(self, task_data: dict):
        """
        Performs a generic task. This is a placeholder.
        Replace this with specific logic relevant to this cell's function.
        """
        print(f"\nGenericCell '{self.cell_id}': Received task with data: {task_data}")

        # Example: Accessing a DNA principle (uncomment and adapt if dna.principles is used)
        # from dna import principles # Import locally if not class-level
        # if "some_value" in task_data and task_data["some_value"] > principles.SOME_THRESHOLD_FROM_DNA:
        #     print(f"Cell '{self.cell_id}': DNA-based threshold exceeded for 'some_value'.")

        # Simulate processing based on task_data
        action_performed = task_data.get('action', 'unknown_action') # Capture the action
        processed_info = f"Task '{action_performed}' processed by {self.cell_id}."
        result = {"status": "success", "cell_id": self.cell_id, "action_performed": action_performed, "input_data": task_data, "processed_info": processed_info}
        print(f"GenericCell '{self.cell_id}': Task completed. Result: {result}")

        # Publish a completion event
        # Event type now includes the action performed for more specific subscriptions
        self.event_bus.publish(f"{self.cell_id}.{action_performed}.complete", result)
        return result
