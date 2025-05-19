# Monitoring Dashboard Setup and Usage

This document provides instructions on how to set up and use the monitoring dashboard included in the AI CI/CD Pipeline project. The dashboard helps you track key performance and reliability metrics for your deployed AI agents.

---

## 1. Configuration

- The dashboard is configured via `monitoring/dashboard_config.json`.
- You can define which metrics to track, their types, units, update intervals, and alert thresholds in this file.
- Example metrics include Response Time, Success Rate, Error Rate, and Request Count.

---

## 2. Installing Dependencies

Make sure you have all required Python packages installed:

```sh
pip install -r requirements.txt
```

---

## 3. Running the Dashboard

Navigate to your project root and start the dashboard with:

```sh
python monitoring/dashboard.py
```

- The dashboard will be available at [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your web browser.
- Ensure your AI agent or pipeline writes live metrics to `monitoring/metrics.json` in the format:
  ```json
  {
    "Response Time": 120,
    "Success Rate": 98.5,
    "Error Rate": 1.5,
    "Request Count": 2345
  }
  ```

---

## 4. Metrics Tracked

The dashboard tracks the following key metrics (configurable):

- **Response Time**: Time taken by the AI agent to respond to requests (ms).
- **Success Rate**: Percentage of successful responses (%).
- **Error Rate**: Percentage of errors encountered during requests (%).
- **Request Count**: Total number of requests received (count).

You can add or modify metrics in `dashboard_config.json`.

---

## 5. Interpreting the Dashboard

- **Metric Cards**: Each metric is displayed as a card, color-coded based on alert thresholds (warning/critical).
- **Graphs**: The dashboard can display graphs (e.g., Response Time over time).
- **Alerts**: Cards change color if a metric exceeds its warning or critical threshold.

---

## 6. Troubleshooting

If you encounter issues:

- Check `dashboard_config.json` for correct JSON syntax and valid metric definitions.
- Ensure all dependencies are installed (`pip install -r requirements.txt`).
- Make sure `metrics.json` exists and is being updated by your agent.
- Review the terminal or browser console for error messages.

---

## 7. Customization

- **To add new metrics:** Edit `dashboard_config.json` and restart the dashboard.
- **To change thresholds or update interval:** Edit the relevant fields in the config file.
- **To connect to a different data source:** Modify `dashboard.py` to read from an API or database.

---

For further assistance, refer to the main project documentation or open an issue in the repository.