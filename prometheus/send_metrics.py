import time
from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

# Define Pushgateway URL (running locally)
PUSHGATEWAY_URL = "http://localhost:9091"

# Create a Prometheus registry and metric
registry = CollectorRegistry()
custom_metric = Gauge("custom_metric", "My custom metric", registry=registry)
custom_counter = Counter(
    "custom_counter_metric",
    "Example Counter Metric",
    registry=registry
)

# Send metric every 10 seconds
while True:
    custom_metric.set(45)  # Set metric value
    custom_counter.inc()
    push_to_gateway(f"{PUSHGATEWAY_URL}", job="custom_job", registry=registry)
    print("Metric pushed to Pushgateway")
    time.sleep(10)  # Send every 10 seconds