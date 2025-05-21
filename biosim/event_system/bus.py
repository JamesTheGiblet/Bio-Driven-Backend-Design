"""
bus.py

Represents the Event Bus / Smart Messaging Layer for the system.
Allows different components (Cells/Organs) to communicate asynchronously.
"""

class EventBus:
    def __init__(self):
        self._subscribers = {}
        print(f"EventBus initialized.")

    def subscribe(self, event_type: str, callback_func):
        """Subscribes a callback function to a specific event type."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback_func)
        # print(f"Subscription: {{callback_func.__name__}} to event '{{event_type}}'") # Uncomment for debugging

    def publish(self, event_type: str, data=None):
        """Publishes an event to all subscribed callbacks."""
        if event_type in self._subscribers:
            # print(f"EventBus: Publishing event '{{event_type}}' with data: {{data}}") # Uncomment for debugging
            for callback_func in self._subscribers[event_type]:
                try:
                    callback_func(data)
                except Exception as e:
                    print(f"Error in subscriber {{callback_func.__name__}} for event '{{event_type}}': {{e}}")
        # else:
            # print(f"EventBus: No subscribers for event '{{event_type}}'") # Uncomment for debugging
