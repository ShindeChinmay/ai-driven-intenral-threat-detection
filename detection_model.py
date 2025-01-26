import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(input_file, output_file):
    """
    Detects anomalies in the structured log data using the Isolation Forest model.
    Args:
    - input_file (str): Path to the structured logs CSV.
    - output_file (str): Path to save the results with anomaly scores.
    """
    # Load the structured log data
    structured_data = pd.read_csv(input_file)

    # Select numeric features for anomaly detection (hour, day_of_week, action_count)
    features = structured_data[['hour', 'day_of_week', 'action_count']]

    # Train the Isolation Forest model to detect anomalies
    model = IsolationForest(contamination=0.05)  # Set contamination rate to 5% (for anomaly ratio)
    structured_data['anomaly_score'] = model.fit_predict(features)

    # Save the detection results with anomaly scores
    structured_data.to_csv(output_file, index=False)

    print(f"Anomaly detection complete. Results saved to {output_file}")

# Example of running the anomaly detection
if __name__ == "__main__":
    detect_anomalies('data/structured_logs.csv', 'data/detection_results.csv')
