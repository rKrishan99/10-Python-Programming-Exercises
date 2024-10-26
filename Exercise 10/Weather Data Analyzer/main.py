import csv

class WeatherData:
    def __init__(self):
        """Initialize an empty tuple to store temperature data."""
        self.temperatures = ()  # Tuple to store temperature data

    def input_temperatures(self):
        """Collect temperature data for a week from user input."""
        temps = []
        for day in range(1, 8):  # Collect temperatures for 7 days
            while True:
                try:
                    temp = float(input(f"Enter the temperature for day {day}: "))  # Input temperature
                    temps.append(temp)  # Add the temperature to the list
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Please enter a valid number.")  # Handle invalid input
        self.temperatures = tuple(temps)  # Convert list to tuple

    def average_temperature(self):
        """Calculate the average temperature for the week."""
        if not self.temperatures:
            return 0  # Return 0 if no temperatures are recorded
        return sum(self.temperatures) / len(self.temperatures)  # Calculate average

    def highest_temperature(self):
        """Get the highest temperature recorded for the week."""
        if not self.temperatures:
            return None  # Return None if no temperatures are recorded
        return max(self.temperatures)  # Get the maximum temperature

    def lowest_temperature(self):
        """Get the lowest temperature recorded for the week."""
        if not self.temperatures:
            return None  # Return None if no temperatures are recorded
        return min(self.temperatures)  # Get the minimum temperature

    def save_to_csv(self, filename='weather_data.csv'):
        """Save the temperature data to a CSV file."""
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Day', 'Temperature'])  # Write header
            for day, temp in enumerate(self.temperatures, start=1):
                writer.writerow([day, temp])  # Write day and temperature data
        print(f"Temperature data saved to {filename}.")

    def load_from_csv(self, filename='weather_data.csv'):
        """Load temperature data from a CSV file."""
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                temps = []
                for row in reader:
                    temps.append(float(row[1]))  # Read temperature data
                self.temperatures = tuple(temps)  # Convert to tuple
            print(f"Temperature data loaded from {filename}.")
        except (FileNotFoundError, ValueError):
            print(f"Error loading data from {filename}. Please check the file.")

    def display_csv_data(self, filename='weather_data.csv'):
        """Display the data stored in the CSV file."""
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                print("\nCSV Data:")
                for row in reader:
                    print(row)  # Print each row in the CSV
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")

def weather_data_analyzer():
    """Main function to manage the Weather Data Analyzer."""
    weather_data = WeatherData()  # Create a WeatherData instance

    while True:
        print("\nOptions:")
        print("1. Input temperatures for the week")
        print("2. Calculate average temperature")
        print("3. Get highest temperature")
        print("4. Get lowest temperature")
        print("5. Save data to CSV")
        print("6. Load data from CSV")
        print("7. Display CSV data")
        print("8. Exit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == '1':
            weather_data.input_temperatures()  # Input temperatures

        elif choice == '2':
            avg_temp = weather_data.average_temperature()  # Calculate average
            print(f"Average temperature: {avg_temp:.2f}")

        elif choice == '3':
            high_temp = weather_data.highest_temperature()  # Get highest temperature
            print(f"Highest temperature: {high_temp:.2f}")

        elif choice == '4':
            low_temp = weather_data.lowest_temperature()  # Get lowest temperature
            print(f"Lowest temperature: {low_temp:.2f}")

        elif choice == '5':
            weather_data.save_to_csv()  # Save data to CSV

        elif choice == '6':
            weather_data.load_from_csv()  # Load data from CSV

        elif choice == '7':
            weather_data.display_csv_data()  # Display CSV data

        elif choice == '8':
            print("Exiting the Weather Data Analyzer.")
            break

        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    weather_data_analyzer()
