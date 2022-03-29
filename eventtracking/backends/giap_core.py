"""Event tracking backend that sends events to GIAP platform"""
import requests
from datetime import timezone
GIAP_CORE_URL = "https://analytics.steamforvietnam.org/events"
class GiapCoreBackend:
    """
        Send events to analytics.steamforvietnam.org
    """
    def __init__(self, **kwargs):
        self.endpoint = kwargs.get("endpoint", GIAP_CORE_URL)
        self.uuid = kwargs.get("uuid", None)

    def send(self, event):
        event_data = {
            "$name": event["name"], "event_type": event["event_type"],
            "$time": int(event["time"].replace(tzinfo=timezone.utc).timestamp() * 1000),
            "$distinct_id": self.uuid,
            "context": event["context"],
            "event": event["event"]
        }
        headers = {"Authorization": f"Bearer {self.uuid}"}
        requests.post(self.endpoint, json={"events": [event_data]}, headers=headers)