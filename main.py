from src.preprocess import load_dataset, preprocess_data
from src.flags_detector import detect_anomalies
from src.visualization import plot_tcp_flags_distribution

# Set dataset file path
dataset_path = "data/54/capture20110815-3.binetflow"

# Load & preprocess dataset
df = load_dataset(dataset_path)
df = preprocess_data(df)

# Detect anomalies
anomalies = detect_anomalies(df)

# Save detected anomalies
anomalies.to_csv("results/anomalies_detected.csv", index=False)

# Plot flag distributions
plot_tcp_flags_distribution(anomalies)

print("Anomaly detection completed. Results saved in 'results/anomalies_detected.csv'.")
