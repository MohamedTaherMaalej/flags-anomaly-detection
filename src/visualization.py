import matplotlib.pyplot as plt
import seaborn as sns

def plot_tcp_flags_distribution(flag_counts):
    """Plots TCP flag distributions."""
    plt.figure(figsize=(12,6))
    sns.boxplot(data=flag_counts.drop(columns=['SrcAddr']))
    plt.title("Distribution of TCP Flags in CTU-13 Dataset")
    plt.xlabel("TCP Flags")
    plt.ylabel("Count")
    plt.show()
