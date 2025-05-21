"""
bdbd_glossary.py

A dictionary defining the core components of Bio-Driven Backend Design (BDBD)
with their definitions, examples, and characteristics.
This serves as a reference for understanding and applying BDBD principles.
"""

BDBD_COMPONENT_GLOSSARY = {
    "DNA": {
        "definition": "Core rules, system principles, and design contracts that govern the entire system.",
        "examples": [
            "Global configuration files (e.g., default retry counts, timeout settings)",
            "API schemas and versioning contracts",
            "Core business logic that is fundamental and rarely changes",
            "Security policies and compliance rules",
            "System-wide constants and enumerations"
        ],
        "characteristics": ["Immutable or rarely changing", "System-wide scope", "Foundation for behavior"]
    },
    "Cells": {
        "definition": "Modular, independent services or components responsible for specific, well-defined business logic or functionality.",
        "examples": [
            "A microservice handling user authentication",
            "A function processing image uploads",
            "A module managing product inventory",
            "A data transformation pipeline stage"
        ],
        "characteristics": ["Encapsulated logic", "Independently deployable/manageable (ideally)", "Clear interfaces", "Focused responsibility"]
    },
    "Organs": {
        "definition": "A collection of related Cells working together to perform a larger, more complex system function. An Organ is a higher-level abstraction of modularity.",
        "examples": [
            "An 'Order Processing System' (Organ) composed of 'PaymentCell', 'InventoryCheckCell', and 'NotificationCell'",
            "A 'User Management System' (Organ) comprising 'RegistrationCell', 'ProfileCell', and 'PermissionsCell'"
        ],
        "characteristics": ["Composed of multiple Cells", "Represents a significant business capability", "Coordinated internal interactions"]
    },
    "Blood Flow": {
        "definition": "Data pipelines and structured messaging systems responsible for the movement of data throughout the system.",
        "examples": [
            "Message queues (e.g., Kafka, RabbitMQ, SQS) for asynchronous data transfer",
            "ETL (Extract, Transform, Load) pipelines",
            "Streaming data platforms (e.g., Apache Flink, Spark Streaming)",
            "Well-defined data formats and schemas for transit"
        ],
        "characteristics": ["Data transport", "Structured information", "Can be synchronous or asynchronous", "Connects Cells/Organs"]
    },
    "Neural Network": {
        "definition": "The event bus or smart messaging layer that enables Cells and Organs to communicate and react to events in a decoupled manner.",
        "examples": [
            "A system-wide event bus implementation (e.g., using a library or custom)",
            "Publish/subscribe messaging patterns",
            "Webhook systems for inter-service notification"
        ],
        "characteristics": ["Decoupled communication", "Event-driven interactions", "Asynchronous (often)", "Enables reactivity"]
    },
    "Immune System": {
        "definition": "Mechanisms for security monitoring, anomaly detection, and threat response.",
        "examples": [
            "Intrusion Detection Systems (IDS)",
            "Web Application Firewalls (WAF)",
            "Security Information and Event Management (SIEM) systems",
            "Automated scripts for identifying and isolating compromised Cells",
            "Rate limiting and abuse detection services"
        ],
        "characteristics": ["Protective", "Reactive to threats", "Monitors system health from a security perspective"]
    },
    "Cell Recycling": {
        "definition": "Processes for lifecycle management, resource cleanup, and decommissioning of unused or unhealthy components.",
        "examples": [
            "Automated scaling down of services based on low demand",
            "Garbage collection for unused data or resources",
            "Archiving or sunsetting policies for old Cells/features",
            "Health checks that trigger decommissioning of failed instances"
        ],
        "characteristics": ["Resource optimization", "Maintains system efficiency", "Removes waste/obsolescence"]
    },
    "Cerebral Cortex": {
        "definition": "The AI-driven layer responsible for higher-level system orchestration, behavior adjustment, learning, and control.",
        "examples": [
            "An AI agent that dynamically adjusts resource allocation based on predictive models",
            "A reinforcement learning system optimizing API routing",
            "A central policy engine that adapts system behavior based on observed events",
            "AI models that manage feature toggles or A/B testing strategies"
        ],
        "characteristics": ["Intelligent control", "Adaptive", "Learning capability", "System-wide optimization", "Orchestration"]
    }
}

# Example usage (if this file were run directly):
# if __name__ == "__main__":
#     print("BDBD Component Glossary:")
#     for component, details in BDBD_COMPONENT_GLOSSARY.items():
#         print(f"\n--- {component} ---")
#         print(f"  Definition: {details['definition']}")
#         print(f"  Examples: {', '.join(details['examples'])}")
#         print(f"  Characteristics: {', '.join(details['characteristics'])}")
