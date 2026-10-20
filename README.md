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

Current Status: Core implementation completed — data validation, cleaning, security analysis, detection engineering, risk scoring, alert generation, RCA, MITRE mapping, and SOC L1 investigation completed.

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


## Implementation Results

### Dataset Processing

- Original records: 1,048,575
- Repeated header rows removed: 1
- Exact duplicate rows removed: 147,586
- Final cleaned records: 900,988
- Invalid timestamps: 0

### Cleaned Traffic Distribution

- Benign: 446,653
- DoS attacks-Hulk: 434,873
- DoS attacks-SlowHTTPTest: 19,462

### Detection Engine V2

The detection engine evaluates multiple network-flow indicators including:

- High packet rate
- High byte rate
- Short flow duration
- High forward packet volume
- High backward packet volume
- Large packet size

Risk scores are generated from the number of triggered indicators.

Results:

- Normal records: 871,348
- Suspicious records: 29,640
- True positives: 27,279
- False-positive candidates: 2,361
- Precision on selected alert set: 92.03%
- Overall recall: approximately 6.01%

The precision figure represents the selected alert set only and is not overall detection accuracy.

## SOC L1 Investigation Workflow

1. Validate the alert
2. Review timestamp and network flow
3. Identify source and destination information
4. Review protocol and destination port
5. Examine traffic indicators
6. Calculate risk level
7. Compare against dataset ground truth during offline evaluation
8. Identify potential false positives
9. Map relevant activity to MITRE ATT&CK
10. Determine L1 disposition
11. Escalate confirmed suspicious activity to L2
12. Document investigation evidence and recommendations

## Root Cause & False-Positive Analysis

The project includes an L1 root-cause analysis stage that separates traffic matching the attack ground truth from benign traffic that triggered detection thresholds.

Benign alerts are classified as false-positive candidates and require contextual validation before closure. Traffic matching non-benign ground truth is marked for further investigation and potential L2 escalation.

## MITRE ATT&CK

The analyzed DoS traffic is mapped to:

- T1498 — Network Denial of Service

The mapping is based on observed network-flow characteristics. The dataset does not independently prove attacker identity, intent, persistence, credential theft, or command execution.

## Project Visualizations

Automated visualizations are generated by  and stored in .

1.  — traffic and attack distribution
2.  — normal vs suspicious detection results
3.  — risk-score distribution
4.  — alert severity distribution
5.  — detected indicator combinations
6.  — SOC L1 alert disposition
7.  — precision and overall recall

## Detection Engineering Assessment

The project deliberately evaluates detection rules instead of assuming that a threshold is effective.

Initial threshold experiments produced high precision but poor recall. Detection Engine V2 improved the selected alert-set precision to 92.03%, while overall recall remained approximately 6.01%.

This demonstrates an important SOC detection-engineering principle: reducing false positives does not automatically mean that a detector has strong coverage.

The current implementation is therefore treated as a cybersecurity research and portfolio lab rather than a production-ready detection control.

## Reproducibility

Create a Python virtual environment and install the project dependencies:



Place the required CSE-CIC-IDS2018 dataset file under  and run the processing pipeline from the project root.

Example commands:



## Key Skills Demonstrated

- SOC L1 alert triage
- Security data analysis
- Network traffic analysis
- Detection engineering
- False-positive analysis
- Risk scoring
- Automated alert generation
- Root-cause analysis
- MITRE ATT&CK mapping
- Incident investigation
- Python automation
- Pandas-based security analytics
- Linux
- Git and GitHub

## Limitations

- The project is based on an offline cybersecurity research dataset.
- Detection thresholds were developed and evaluated using the available dataset labels.
- The current detector has limited overall recall and should not be represented as a production IDS/IPS or SIEM detection rule.
- Ground-truth labels are used for offline evaluation and are not available in a real-time SOC environment.
- Additional datasets, contextual enrichment, threat intelligence, asset criticality, and time-window correlation would be required for a production-grade detection platform.
