"""
orchestrator.py

Represents a simplified Cerebral Cortex for biosim.
It orchestrates Cells, subscribes to events, and makes decisions.
This is a foundational template.
"""

# from event_system.bus import EventBus # For type hinting
# from cells.generic_cell import GenericCell # For type hinting
# from dna import principles # If DNA principles are directly used by Cortex

class CortexOrchestrator:
    def __init__(self, event_bus): # Consider adding type hint: event_bus: EventBus
        self.event_bus = event_bus
        self.cells = {} # Stores registered cell instances: {'cell_id': cell_instance}
        print(f"CortexOrchestrator for biosim initialized.")

        # Subscriptions will now be more specific and handled in main.py
        # or dynamically if the Cortex becomes more advanced.
        
    def register_cell(self, cell): # Consider adding type hint: cell: GenericCell
        """Registers a cell with the orchestrator."""
        if hasattr(cell, 'cell_id'):
            self.cells[cell.cell_id] = cell
            print(f"Cortex: Registered Cell '{cell.cell_id}'")
        else:
            print("Cortex: Error - Cell object to be registered does not have a 'cell_id' attribute.")


    def delegate_task_to_cell(self, cell_id: str, task_data: dict):
        """Instructs a specific cell to perform a task."""
        target_cell = self.cells.get(cell_id)
        if target_cell:
            print(f"\nCortex: Delegating task to Cell '{cell_id}' with data: {task_data}")
            # Assuming the cell has a method like 'perform_task'
            if hasattr(target_cell, 'perform_task') and callable(getattr(target_cell, 'perform_task')):
                return target_cell.perform_task(task_data)
            else:
                print(f"Cortex: Error - Cell '{cell_id}' does not have a callable 'perform_task' method.")
                return None
        else:
            print(f"Cortex: Error - Cell '{cell_id}' not found.")
            return None

    def handle_data_analysis_complete(self, event_data):
        """
        Handles completion of a 'analyze_data' task and may trigger a notification.
        """
        cell_id = event_data.get('cell_id', 'UnknownCell')
        print(f"Cortex: Received 'analyze_data.complete' event from '{cell_id}'. Data: {event_data}")

        if event_data.get('status') == 'success':
            # Decision: If data analysis was successful, trigger a notification.
            # In a real system, the target notifier cell might be determined by DNA principles or other logic.
            notifier_cell_id = "notifier_beta" # Assuming this cell is registered
            if notifier_cell_id in self.cells:
                print(f"Cortex: Data analysis by '{cell_id}' successful. Triggering notification via '{notifier_cell_id}'.")
                notification_payload = {
                    "action": "send_notification",
                    "recipient": "admin@example.com", # Could come from DNA or event_data
                    "message": f"Analysis by {cell_id} for action '{event_data.get('action_performed')}' complete. Details: {event_data.get('processed_info')}"
                }
                self.delegate_task_to_cell(notifier_cell_id, notification_payload)
            else:
                print(f"Cortex: Warning - Notifier cell '{notifier_cell_id}' not found for chaining.")

    def handle_notification_sent(self, event_data):
        """Handles completion of a 'send_notification' task."""
        cell_id = event_data.get('cell_id', 'UnknownCell')
        print(f"Cortex: Received 'send_notification.complete' event from '{cell_id}'. Notification details: {event_data.get('processed_info')}")
