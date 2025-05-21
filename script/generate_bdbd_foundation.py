import os
import stat

# --- Boilerplate Content ---

DNA_PRINCIPLES_CONTENT = """\"\"\"
principles.py

Defines the Core Rules and System Principles (DNA) for {system_name}.
These are fundamental, often immutable, guidelines or configurations.
\"\"\"

# Example: System-wide constants
SYSTEM_NAME = "{system_name}"
SYSTEM_VERSION = "0.1.0"
DEFAULT_LOG_LEVEL = "INFO"

# Add other foundational principles specific to your system's domain
# E.g., MAX_CONNECTIONS, DEFAULT_TIMEOUT, DATA_SCHEMA_VERSION, etc.
"""

EVENT_BUS_CONTENT = """\"\"\"
bus.py

Represents the Event Bus / Smart Messaging Layer for the system.
Allows different components (Cells/Organs) to communicate asynchronously.
\"\"\"

class EventBus:
    def __init__(self):
        self._subscribers = {}
        print(f"EventBus initialized.")

    def subscribe(self, event_type: str, callback_func):
        \"\"\"Subscribes a callback function to a specific event type.\"\"\"
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback_func)
        # print(f"Subscription: {{callback_func.__name__}} to event '{{event_type}}'") # Uncomment for debugging

    def publish(self, event_type: str, data=None):
        \"\"\"Publishes an event to all subscribed callbacks.\"\"\"
        if event_type in self._subscribers:
            # print(f"EventBus: Publishing event '{{event_type}}' with data: {{data}}") # Uncomment for debugging
            for callback_func in self._subscribers[event_type]:
                try:
                    callback_func(data)
                except Exception as e:
                    print(f"Error in subscriber {{callback_func.__name__}} for event '{{event_type}}': {{e}}")
        # else:
            # print(f"EventBus: No subscribers for event '{{event_type}}'") # Uncomment for debugging
"""

CELLS_INIT_CONTENT = """# This file makes the 'cells' directory a Python package.
# You can import cells from here, e.g.:
# from .generic_cell import GenericCell
"""

GENERIC_CELL_CONTENT = """\"\"\"
generic_cell.py

A template for a modular service (Cell / Organ) in {system_name}.
It handles specific business logic, interacts with DNA principles,
and communicates via the Event Bus.
\"\"\"

# from dna import principles # Import if this cell needs direct access to DNA
# from event_system.bus import EventBus # For type hinting if you use it

class GenericCell:
    def __init__(self, cell_id: str, event_bus): # Consider adding type hint: event_bus: EventBus
        self.cell_id = cell_id
        self.event_bus = event_bus
        print(f"GenericCell '{{self.cell_id}}' initialized.")

    def perform_task(self, task_data: dict):
        \"\"\"
        Performs a generic task. This is a placeholder.
        Replace this with specific logic relevant to this cell's function.
        \"\"\"
        print(f"\\nGenericCell '{{self.cell_id}}': Received task with data: {{task_data}}")

        # Example: Accessing a DNA principle (uncomment and adapt if dna.principles is used)
        # from dna import principles # Import locally if not class-level
        # if "some_value" in task_data and task_data["some_value"] > principles.SOME_THRESHOLD_FROM_DNA:
        #     print(f"Cell '{{self.cell_id}}': DNA-based threshold exceeded for 'some_value'.")

        # Simulate processing based on task_data
        processed_info = f"Task '{{task_data.get('action', 'unknown_action')}}' processed by {{self.cell_id}}."
        result = {{"status": "success", "cell_id": self.cell_id, "input_data": task_data, "processed_info": processed_info}}
        print(f"GenericCell '{{self.cell_id}}': Task completed. Result: {{result}}")

        # Publish a completion event
        # Choose a meaningful event_type for your system, e.g., based on cell_id or task type
        self.event_bus.publish(f"{{self.cell_id}}.task.complete", result)
        return result
"""

CORTEX_ORCHESTRATOR_CONTENT = """\"\"\"
orchestrator.py

Represents a simplified Cerebral Cortex for {system_name}.
It orchestrates Cells, subscribes to events, and makes decisions.
This is a foundational template.
\"\"\"

# from event_system.bus import EventBus # For type hinting
# from cells.generic_cell import GenericCell # For type hinting
# from dna import principles # If DNA principles are directly used by Cortex

class CortexOrchestrator:
    def __init__(self, event_bus): # Consider adding type hint: event_bus: EventBus
        self.event_bus = event_bus
        self.cells = {{}} # Stores registered cell instances: {{'cell_id': cell_instance}}
        print(f"CortexOrchestrator for {system_name} initialized.")

        # Example: Subscribe to a generic completion event pattern if your bus supports it,
        # or subscribe to specific events in the main application setup (see main.py).
        # self.event_bus.subscribe("*.task.complete", self.handle_any_task_complete_event)

    def register_cell(self, cell): # Consider adding type hint: cell: GenericCell
        \"\"\"Registers a cell with the orchestrator.\"\"\"
        if hasattr(cell, 'cell_id'):
            self.cells[cell.cell_id] = cell
            print(f"Cortex: Registered Cell '{{cell.cell_id}}'")
        else:
            print("Cortex: Error - Cell object to be registered does not have a 'cell_id' attribute.")


    def delegate_task_to_cell(self, cell_id: str, task_data: dict):
        \"\"\"Instructs a specific cell to perform a task.\"\"\"
        target_cell = self.cells.get(cell_id)
        if target_cell:
            print(f"\\nCortex: Delegating task to Cell '{{cell_id}}' with data: {{task_data}}")
            # Assuming the cell has a method like 'perform_task'
            if hasattr(target_cell, 'perform_task') and callable(getattr(target_cell, 'perform_task')):
                return target_cell.perform_task(task_data)
            else:
                print(f"Cortex: Error - Cell '{{cell_id}}' does not have a callable 'perform_task' method.")
                return None
        else:
            print(f"Cortex: Error - Cell '{{cell_id}}' not found.")
            return None

    def handle_task_complete_event(self, event_data):
        \"\"\"
        Handles generic task completion events from cells.
        This method needs to be subscribed to specific event types in the main setup (see main.py).
        \"\"\"
        cell_id = event_data.get('cell_id', 'UnknownCell')
        print(f"Cortex: Received task completion event from '{{cell_id}}'. Data: {{event_data}}")
        # Add logic here to react to task completions,
        # potentially chain tasks, make higher-level decisions, or trigger AI adaptations.
"""

MAIN_PY_CONTENT = """\"\"\"
main.py

Main entry point for the {system_name} BDBD system.
Demonstrates initialization and basic interaction of components.
This script is intended to be run from the root of the '{system_name}' directory.
\"\"\"
from dna import principles
from event_system.bus import EventBus
from cells.generic_cell import GenericCell # Assuming you have a GenericCell in cells/
from cortex.orchestrator import CortexOrchestrator

def run_system_demo():
    print(f"--- Starting BDBD System Demo for: {{principles.SYSTEM_NAME}} v{{principles.SYSTEM_VERSION}} ---")

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
    # Ensure the event type matches what the cell publishes (e.g., "{{cell_id}}.task.complete")
    event_bus.subscribe(f"{{cell1_id}}.task.complete", cortex.handle_task_complete_event)
    event_bus.subscribe(f"{{cell2_id}}.task.complete", cortex.handle_task_complete_event)
    # You could also have cells subscribe to each other's events if needed.


    # 5. Cortex orchestrates tasks
    # The Cortex delegates work to the appropriate cells.
    print(f"\\nMain: Attempting to delegate 'analyze_data' task to {{cell1_id}}.")
    task1_payload = {{"action": "analyze_data", "source_id": "sensor_A01", "data_points": [1,2,3,4,5]}}
    result1 = cortex.delegate_task_to_cell(cell1_id, task1_payload)

    if result1 and isinstance(result1, dict):
        print(f"\\nMain: Task for {{cell1_id}} ({{task1_payload.get('action')}}) completed with status: {{result1.get('status', 'unknown')}}")
        # Potentially trigger another task based on result1
        if result1.get('status') == 'success':
            print(f"\\nMain: Attempting to delegate 'send_notification' task to {{cell2_id}} based on {{cell1_id}}'s success.")
            task2_payload = {{"action": "send_notification", "recipient": "admin@example.com", "message": f"Analysis by {{cell1_id}} complete."}}
            cortex.delegate_task_to_cell(cell2_id, task2_payload)

    elif result1 is None:
        print(f"\\nMain: Task delegation to {{cell1_id}} failed or cell did not return a result.")
    else:
        print(f"\\nMain: Task delegated to {{cell1_id}} returned an unexpected result type: {{type(result1)}}")


    # Add more complex interactions, error handling, or AI-driven adaptations here as the system evolves.

    print(f"\\n--- BDBD System Demo for: {{principles.SYSTEM_NAME}} Finished ---")

if __name__ == "__main__":
    run_system_demo()
"""

# --- Script Logic ---

def create_file(path, content):
    """Creates a file with the given content, ensuring parent directories exist."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")

def generate_bdbd_foundation(system_name_input):
    """Generates the foundational directory structure and files for a BDBD system."""
    if not system_name_input or not system_name_input.strip():
        print("Error: System name cannot be empty.")
        return

    # Sanitize the system name to be a valid directory name (and Python module name)
    # Replace spaces with underscores, convert to lowercase, keep alphanumeric and underscores
    system_name_formatted_for_code = system_name_input.replace('-', '_').replace(' ', '_') # For use in SYSTEM_NAME variable
    base_path = "".join(c if c.isalnum() or c == '_' else '' for c in system_name_formatted_for_code.lower())

    if not base_path: # If sanitization results in an empty string
        print("Error: Sanitized system name is empty or invalid. Please provide a name with alphanumeric characters.")
        return

    if os.path.exists(base_path):
        print(f"Error: Directory '{base_path}' already exists. Please choose a different name or remove the existing directory.")
        return

    print(f"\\nGenerating BDBD foundation for system: '{system_name_input}' in directory '{base_path}'...")

    # Define paths for the files to be created
    paths = {
        "dna_principles": os.path.join(base_path, "dna", "principles.py"),
        "event_bus": os.path.join(base_path, "event_system", "bus.py"),
        "cells_init": os.path.join(base_path, "cells", "__init__.py"),
        "generic_cell": os.path.join(base_path, "cells", "generic_cell.py"),
        "cortex_orchestrator": os.path.join(base_path, "cortex", "orchestrator.py"),
        "main_py": os.path.join(base_path, "main.py"),
    }

    # Create files with content, replacing placeholders
    # Pass the original system_name_input for display purposes in docstrings/comments
    # and the formatted one for code variables if needed.
    create_file(paths["dna_principles"], DNA_PRINCIPLES_CONTENT.format(system_name=system_name_input))
    create_file(paths["event_bus"], EVENT_BUS_CONTENT) # Event bus content is generic
    create_file(paths["cells_init"], CELLS_INIT_CONTENT)
    create_file(paths["generic_cell"], GENERIC_CELL_CONTENT.format(system_name=system_name_input))
    create_file(paths["cortex_orchestrator"], CORTEX_ORCHESTRATOR_CONTENT.format(system_name=system_name_input))
    create_file(paths["main_py"], MAIN_PY_CONTENT.format(system_name=system_name_input))

    print(f"\\nBDBD foundation for '{system_name_input}' created successfully in '{base_path}'.")
    print("To run the demo for your new system:")
    print(f"1. Navigate into the directory: cd {base_path}")
    print(f"2. Run the main script: python main.py")
    print("\\nNext steps:")
    print(" - Review and customize 'dna/principles.py' with your system's core rules.")
    print(" - Develop specific cell types in the 'cells/' directory, inheriting or adapting from 'generic_cell.py'.")
    print(" - Enhance 'cortex/orchestrator.py' with more sophisticated logic and AI capabilities.")
    print(" - Expand 'main.py' to reflect more complex workflows and interactions.")

if __name__ == "__main__":
    user_system_name = input("Enter the name for your new BDBD system (e.g., 'Inventory Manager', 'BioSim Core'): ")
    generate_bdbd_foundation(user_system_name)
