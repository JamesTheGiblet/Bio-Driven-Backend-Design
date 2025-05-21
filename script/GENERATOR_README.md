# BDBD Foundation Generator (`generate_bdbd_foundation.py`)

## Purpose

This script automates the creation of a foundational directory structure and boilerplate code for new projects adopting the Bio-Driven Backend Design (BDBD) methodology. Its primary goal is to:

- **Ensure Consistency:** Provide a standardized starting point for all BDBD projects.
- **Save Time:** Reduce the manual effort required to set up the initial project files and directories.
- **Promote BDBD Principles:** Embed the core BDBD concepts (DNA, Cells, Event System, Cortex, Glossary) directly into the project structure from the outset.
- **Facilitate Onboarding:** Help developers new to BDBD quickly understand the basic layout and component roles.

## What it Does

When executed, the script will:

1.  **Prompt for a System Name:** Ask the user to provide a name for their new BDBD system (e.g., "Inventory Management System", "BioSim Core").
2.  **Create Root Directory:** Generate a root directory for the new system. The directory name is a sanitized, lowercase version of the provided system name (e.g., `inventory_management_system`).
3.  **Establish Core BDBD Directories:** Inside the root directory, it creates the following subdirectories:
    *   `dna/`: For defining core system principles, rules, and configurations.
    *   `event_system/`: For the event bus or messaging layer.
    *   `cells/`: For modular components or services (the "workhorses" of the system).
    *   `cortex/`: For the orchestration and AI-driven control layer.
    *   `reference/`: For helpful reference materials, including the BDBD glossary.
4.  **Generate Boilerplate Python Files:** Populates these directories with initial Python files:
    *   `dna/principles.py`: A template for system-wide constants and rules.
    *   `event_system/bus.py`: A basic event bus implementation.
    *   `cells/__init__.py`: Makes the `cells` directory a Python package.
    *   `cells/generic_cell.py`: A template for creating BDBD Cells.
    *   `cortex/orchestrator.py`: A basic template for the BDBD Cortex.
    *   `reference/bdbd_glossary.py`: A Python dictionary defining BDBD components, their characteristics, and examples.
    *   `main.py` (in the root directory): A runnable script demonstrating the initialization and basic interaction of the generated components.
5.  **Provide Guidance:** Prints instructions on how to navigate to the new project directory and run the demo `main.py` script, along with suggestions for next steps in development.

## How to Use

1.  **Navigate to the `script/` directory** (or wherever you have saved `generate_bdbd_foundation.py`).
    ```bash
    cd path/to/Bio-Driven-Backend-Design/script
    ```
2.  **Run the script** using Python:
    ```bash
    python generate_bdbd_foundation.py
    ```
3.  **Enter a name** for your new BDBD system when prompted.
4.  The script will create the new project directory and files in the same location where the script is run.
5.  Follow the on-screen instructions to `cd` into your new project directory and run `python main.py` to see the basic demo.

## Customization

The generated files are templates and are meant to be customized:

- **`dna/principles.py`**: Modify this to include the specific core rules and configurations relevant to your system.
- **`cells/generic_cell.py`**: Use this as a base to create specialized Cells tailored to your system's functionalities. You will likely create multiple cell types.
- **`cortex/orchestrator.py`**: Enhance this with more sophisticated orchestration logic, event handling, and eventually, AI-driven adaptive behaviors.
- **`main.py`**: Expand this to reflect the actual workflows and interactions of your system.
- **`reference/bdbd_glossary.py`**: While comprehensive, you can extend this if you develop new BDBD concepts specific to your domain.

This generator provides a solid foundation, allowing you to focus on building the unique aspects of your bio-inspired system.