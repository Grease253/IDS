import socket

# Set up socket variables
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Set up server connection
host = '<host>'
port = <port>
client_socket.connect((host, port))

# Create packet types to filter
packet_types = ["SYN", "ACK", "FIN", "RST"] 

# Create a flag to trigger alarms
alert_flag = False

while True:

    # Monitor network traffic
    network_data = client_socket.recv(1024)

    if not network_data:
        # The server has closed the connection
        break

    # Analyze network packets and packet types
    for packet_type in packet_types:
        if packet_type in network_data:
            # Set alarm flag
            alert_flag = True
            break

    # Check alarm flag and take action
    if alert_flag:
        # Trigger alarm logic (send email, text message, etc.)
        print("Possible Intrusion Detected!")
        # Reset alarm flag
        alert_flag = False

client_socket.close()