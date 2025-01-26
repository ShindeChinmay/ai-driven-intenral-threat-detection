from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    data = pd.read_csv("data/detection_results.csv")
    alerts = data[data['anomaly_score'] == -1]
    return jsonify(alerts.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
