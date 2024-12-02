import time

from azure.iot.device import IoTHubDeviceClient, Message
import json

# Connection string of your IoT device
CONNECTION_STRING = "HostName=eatonditiothub1.azure-devices.net;DeviceId=1b8cb16a-84e3-4d97-ae58-af851c0aece2;SharedAccessKey=LHIvQQO7oAKYtJXSLfwq/Ntk77Vwdi5ziAIoTDRYndY="

# Payload and properties
payload = {
    "d": {
        "d": "1b8cb16a-84e3-4d97-ae58-af851c0aece2",
        "profile": "9a885794-708f-464c-bd03-f1c1c51fe909",
        "name": "My-Gateway",
        "ds": [
            {
                "d": "2e5e2306-f96c-49ec-a826-4b108b267fae",
                "profile": "b8c56f41-d775-45d2-b703-550feee8a83b",
                "name": "DG1-1"
            },
            {
                "d": "6bda3b76-b225-41c4-be03-73246d1c02f6",
                "profile": "bdc82d04-97ae-4b60-ac85-24c42ee4fa9a",
                "name": "DH1-1"
            }
        ]
    }
}

# Initialize the IoT Hub device client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    # Create a message with the payload
    message = Message(json.dumps(payload))

    # Add properties to the message
    message.custom_properties["a"] = "DeviceTree"
    message.custom_properties["p"] = payload["d"]["d"]
    message.custom_properties["del"] = "false"  # Optional, remove this if not needed
    # message.custom_properties["to"] = "minimum_value"  # Optional, remove this if not needed

    # Send the message to IoT Hub
    client.send_message(message)
    print("Message sent successfully!")
    time.sleep(7200)

except Exception as e:
    print(f"Error sending message: {e}")

finally:
    # Disconnect the client
    client.shutdown()