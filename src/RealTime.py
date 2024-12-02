from azure.iot.device import IoTHubDeviceClient, Message
import json

# Connection string of your IoT device
CONNECTION_STRING = "HostName=eatonditiothub1.azure-devices.net;DeviceId=1b8cb16a-84e3-4d97-ae58-af851c0aece2;SharedAccessKey=LHIvQQO7oAKYtJXSLfwq/Ntk77Vwdi5ziAIoTDRYndY="

# Payload and properties
payload = {
        "realtimes": [
            {
                "c": "10363920",
                "t": 1733127439,
                "v": "75"
            }
        ]
    }

# Initialize the IoT Hub device client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    # Create a message with the payload
    message = Message(json.dumps(payload))

    # Add properties to the message
    message.custom_properties["a"] = 'Realtimes'
    message.custom_properties["p"] = '2e5e2306-f96c-49ec-a826-4b108b267fae'

    # Send the message to IoT Hub
    client.send_message(message)
    print("Message sent successfully!")

except Exception as e:
    print(f"Error sending message: {e}")

finally:
    # Disconnect the client
    client.shutdown()