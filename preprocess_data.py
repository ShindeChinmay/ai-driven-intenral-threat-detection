import pandas as pd

def preprocess_logs(input_file, output_file):
    """
    Preprocesses raw log data to generate structured logs with additional features.
    Args:
    - input_file (str): Path to the raw logs CSV.
    - output_file (str): Path to save the processed structured logs CSV.
    """
    # Load the raw log file
    raw_data = pd.read_csv(input_file)

    # Convert timestamp to datetime format
    raw_data['timestamp'] = pd.to_datetime(raw_data['timestamp'])

    # Extract additional features from timestamp
    raw_data['hour'] = raw_data['timestamp'].dt.hour
    raw_data['day_of_week'] = raw_data['timestamp'].dt.dayofweek
    raw_data['action_count'] = raw_data.groupby('user')['action'].transform('count')

    # Drop any rows with missing values (if any)
    structured_data = raw_data.dropna()

    # Save the structured data to a new CSV file
    structured_data.to_csv(output_file, index=False)

    print(f"Preprocessing complete. Structured data saved to {output_file}")

# Example of running the preprocessing
if __name__ == "__main__":
    preprocess_logs('data/raw_logs.csv', 'data/structured_logs.csv')
