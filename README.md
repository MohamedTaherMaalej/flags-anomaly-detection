# Flags Anomaly Detection

## Project Overview

This project focuses on detecting network anomalies using TCP flag analysis. It processes the CTU-13 dataset to identify unusual patterns that may indicate botnet activity or other network intrusions.

## Directory Structure

```plaintext
flags-anomaly-detection/
│── data/  
│   ├── raw/  
│   │   ├── CTU-13-Dataset.tar.bz2  # Original dataset  
│   │   ├── captureXX/  # Extracted dataset folders  
│   │   │   ├── captureXX.csv  
│   ├── processed/  
│   │   ├── cleaned_data.csv  # Preprocessed dataset  
│  
│── src/  # Source code  
│   ├── preprocess.py  # Data extraction & cleaning  
│   ├── flags_detector.py  # Flags anomaly detection logic  
│   ├── visualization.py  # Generate plots  
│  
│── notebooks/  
│   ├── exploratory_analysis.ipynb  # Jupyter Notebook for analysis  
│  
│── results/  
│   ├── anomalies_detected.csv  # Output of flagged anomalies  
│   ├── tcp_flags_distribution.png  # Visualization of TCP flags  
│  
│── main.py  # Main script to run everything  
│── requirements.txt  # Dependencies (Pandas, Matplotlib, Seaborn, etc.)  
│── README.md  # Project documentation  
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MohamedTaherMaalej/flags-anomaly-detection.git
   ```

2. Navigate into the project directory:

   ```bash
   cd flags-anomaly-detection
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to preprocess the dataset and detect anomalies:

```bash
python main.py
```

Alternatively, analyze the dataset interactively using Jupyter Notebook:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## Features

- **Data Preprocessing:** Extract and clean network traffic data.
- **Anomaly Detection:** Uses machine learning to flag suspicious traffic based on TCP flags.
- **Visualization:** Generate insights using graphical representations.

## Results

- The detected anomalies are stored in `results/anomalies_detected.csv`.
- TCP flags distribution visualization is available in `results/tcp_flags_distribution.png`.

## Dataset

- **Source:** CTU-13 dataset
- **Description:** Real-world botnet traffic captured in a controlled environment.

## Contributing

If you'd like to contribute, feel free to fork the repo and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, reach out via GitHub Issues.
