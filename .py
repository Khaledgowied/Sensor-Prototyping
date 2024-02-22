
def get_sensor_reading():
    import random
    return random.uniform(0, 100)                  # Simulate temperature readings between 0°C and 100°C

                              # Process sensor data ( calibration)
def process_sensor_data(reading):
                                               # Simulate calibration process by adding a fixed offset of 2°C
    calibrated_reading = reading + 2
    return calibrated_reading

                                          # Display sensor data
def display_sensor_data(reading):
    print("Temperature Reading:", reading, "°C")

# Main function
def main():
                                          # Continuously read and display sensor data
    while True:
                                                          # Read sensor data
        sensor_reading = get_sensor_reading()
        
                                                 # Process sensor data (including calibration)
        processed_reading = process_sensor_data(sensor_reading)
        
                                           # Display sensor data
        display_sensor_data(processed_reading)

                                                     # Add a delay (simulate real-time operation)
        import time
        time.sleep(1)                     # Sleep for 1 second

                            # Run the main function
if __name__ == "__main__":
    main()
