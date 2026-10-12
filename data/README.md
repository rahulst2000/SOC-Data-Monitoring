# Dataset

This project uses the **CSE-CIC-IDS2018** cybersecurity dataset.

The dataset is publicly available through the AWS Open Data Registry and was developed for cybersecurity research by the Canadian Institute for Cybersecurity.

## Dataset Purpose

The dataset contains network traffic and machine-log data representing benign activity and multiple cyberattack scenarios.

The project uses the dataset for:

- Security data analysis
- Attack detection
- Anomaly analysis
- Risk scoring
- Alert generation
- Root-cause investigation
- SOC investigation workflows

## Dataset Policy

The original dataset is **not committed to this GitHub repository** because of its size.

Download the dataset from the official source and place the required files under the local `data/` directory.

## Official Source

CSE-CIC-IDS2018:
https://registry.opendata.aws/cse-cic-ids2018/

## Local Structure

Expected local structure:

data/
├── README.md
└── <downloaded dataset files>

The downloaded dataset files are excluded from Git using `.gitignore`.
