import os

from dotenv import load_dotenv
from azure.monitor.opentelemetry import configure_azure_monitor

load_dotenv()

configure_azure_monitor(
    connection_string=os.getenv(
        "APPLICATIONINSIGHTS_CONNECTION_STRING"
    )
)