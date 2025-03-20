import pandas as pd

def detect_anomalies(df):
    """Detect anomalies based on TCP flag distributions."""
    tcp_flags = ['S', 'A', 'F', 'R', 'P', 'U', 'E', 'C']
    
    # Count occurrences of each TCP flag per source IP
    for flag in tcp_flags:
        df[flag] = df['State'].str.contains(flag, na=False).astype(int)

    flag_counts = df.groupby('SrcAddr')[tcp_flags].sum().reset_index()
    
    # Compute anomaly score (high SYN or RST rates)
    flag_counts['AnomalyScore'] = flag_counts['S'] * 2 + flag_counts['R'] * 3 - flag_counts['A']

    # Define anomaly threshold (top 5% most anomalous)
    threshold = flag_counts['AnomalyScore'].quantile(0.95)
    anomalies = flag_counts[flag_counts['AnomalyScore'] > threshold]

    print(f"Detected {len(anomalies)} anomalous IPs.")
    
    return anomalies
