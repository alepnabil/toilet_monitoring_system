import serial


serialPort = serial.Serial('COM6', 9600)  # Replace 'COM6' with the appropriate port

while True:
    # Read line from serial port
    line = serialPort.readline().decode('latin-1').strip()
    data = line.split('\t')