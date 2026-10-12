# Security Data Monitoring & SOC Investigation Platform

A Python-based security monitoring and investigation platform built using the publicly available CSE-CIC-IDS2018 cybersecurity dataset.

## Project Objective

The objective of this project is to build a practical security-data monitoring pipeline that transforms large-scale network security data into actionable SOC investigation results.

The project demonstrates skills relevant to:

- SOC Analyst L1
- SOC Analyst L2
- Security Operations
- Security Monitoring
- Detection Engineering
- Security Data Analysis
- Security Automation

## Architecture

CSE-CIC-IDS2018 Dataset
        |
        v
Data Ingestion
        |
        v
Data Validation
        |
        v
Cleaning & Normalization
        |
        v
Security Data Analysis
        |
        v
Threat Detection
        |
        v
Anomaly Detection
        |
        v
Risk Scoring
        |
        v
Automated Alerting
        |
        v
Root Cause Analysis
        |
        v
SOC Investigation
        |
        v
Incident Reporting

## Key Capabilities

The platform will support:

- Large-scale security data ingestion
- Data quality validation
- Data cleaning and normalization
- Network traffic analysis
- Benign vs attack analysis
- Threat detection
- Anomaly detection
- Risk scoring
- Automated alert generation
- Root-cause analysis
- Security investigation
- MITRE ATT&CK mapping
- Incident documentation

## Dataset

This project uses the CSE-CIC-IDS2018 cybersecurity research dataset.

The dataset contains network traffic and machine-log data representing benign activity and multiple cyberattack scenarios.

Attack scenarios include:

- Brute Force
- Heartbleed
- Botnet
- DoS
- DDoS
- Web attacks
- Infiltration

The original dataset is not stored in this repository because of its size.

Dataset documentation:

data/README.md

Official dataset source:

https://registry.opendata.aws/cse-cic-ids2018/

## Technology Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Security

- Network Security
- Threat Detection
- Anomaly Detection
- SOC Investigation
- MITRE ATT&CK

### Environment

- Linux
- Git
- GitHub

## Repository Structure

SOC-Data-Monitoring/
|
├── data/
│   └── README.md
|
├── investigation/
|
├── reports/
|
├── screenshots/
|
├── src/
|
├── .gitignore
├── README.md
└── requirements.txt

## Development Roadmap

### Phase 1 - Project Foundation

- [x] Project structure
- [x] Python dependencies
- [x] Git configuration
- [x] Dataset documentation
- [x] Repository documentation

### Phase 2 - Dataset Acquisition

- [ ] Obtain CSE-CIC-IDS2018
- [ ] Identify relevant dataset files
- [ ] Inspect dataset structure
- [ ] Document available fields
- [ ] Establish data ingestion process

### Phase 3 - Data Engineering

- [ ] Data validation
- [ ] Missing-value analysis
- [ ] Duplicate detection
- [ ] Data type validation
- [ ] Cleaning
- [ ] Normalization

### Phase 4 - Security Analysis

- [ ] Traffic profiling
- [ ] Benign activity analysis
- [ ] Attack distribution analysis
- [ ] Source/destination analysis
- [ ] Protocol analysis
- [ ] Feature analysis

### Phase 5 - Threat Detection

- [ ] Attack detection rules
- [ ] Anomaly detection
- [ ] Suspicious traffic identification
- [ ] Detection thresholds
- [ ] Detection validation

### Phase 6 - SOC Automation

- [ ] Risk scoring
- [ ] Alert generation
- [ ] Alert prioritization
- [ ] Investigation workflow
- [ ] Root-cause analysis
- [ ] MITRE ATT&CK mapping

### Phase 7 - Reporting

- [ ] Investigation timelines
- [ ] IOC extraction
- [ ] Incident reports
- [ ] Detection evidence
- [ ] SOC investigation screenshots
- [ ] Final project documentation

## Project Status

Current Status: Project foundation completed.

The repository has been intentionally kept clean before dataset acquisition.

CSE-CIC-IDS2018 is the primary dataset for this project.

No synthetic security dataset is used as the primary project dataset.

## Data and Repository Policy

Large datasets are excluded from GitHub.

Generated analysis files and temporary investigation artifacts are excluded where appropriate.

The repository contains source code, documentation, investigation methodology, and reproducible project structure rather than redistributing the original dataset.

## Disclaimer

This project is intended for cybersecurity education, research, portfolio development, and authorized security analysis.

All analysis should be performed only on datasets and systems for which appropriate permission has been granted.

## Author

Rahul S T

B.E. - Artificial Intelligence & Data Science

Focus Areas:

- Security Operations
- SOC Analysis
- Threat Detection
- Security Automation
- Python
- Data Analysis
