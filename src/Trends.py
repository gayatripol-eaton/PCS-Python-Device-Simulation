from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import json
import asyncio

# Define connection string
connectionString = "HostName=eatonditiothub1.azure-devices.net;DeviceId=ea687a34-db8c-4a28-920e-136a07260d7c;SharedAccessKey=tGoBDYbycRRby6orWhJOLdeFgoxMK/tD4AIoTBFPQdU="


async def sendToIotHub(data):
    try:
        # Create an instance of the IoT Hub Client class
        device_client = IoTHubDeviceClient.create_from_connection_string(connectionString)

        # Connect the device client
        await device_client.connect()

        # Send the message
        await device_client.send_message(data)
        print("Message sent to IoT Hub:", data)

        # Shutdown the client
        await device_client.shutdown()

    except Exception as e:
        print("Error:", str(e))


def main():
    data = {
        "trends": [
            {
                "c": "10363920",
                "t": 1732879565,
                "v": "50"
            }
        ]
    }

    json_data = json.dumps(data)
    message = Message(json_data.encode('ascii'))
    message.custom_properties['a'] = 'Trends'
    message.custom_properties['p'] = '5d583d4e-a07f-47c2-8189-b67cd361391f'
    message.custom_properties["del"] = "false"

    asyncio.run(sendToIotHub(json_data))


if __name__ == '__main__':
    main()