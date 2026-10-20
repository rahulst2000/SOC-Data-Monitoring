# MITRE ATT&CK Mapping

## Project Scope

This project analyzes network traffic from the CSE-CIC-IDS2018
dataset and performs SOC L1-style detection and investigation.

The downloaded dataset subset contains:

- Benign traffic
- DoS attacks-Hulk
- DoS attacks-SlowHTTPTest

MITRE ATT&CK mappings are therefore limited to behaviors supported
by the available network-traffic evidence.

---

## Detection Mapping

| Dataset / Detection | Observed Behavior | MITRE ATT&CK | Technique |
|---|---|---|---|
| DoS attacks-Hulk | High-volume network traffic intended to exhaust the target | T1498 | Network Denial of Service |
| DoS attacks-SlowHTTPTest | Denial-of-service behavior against a network service | T1498 | Network Denial of Service |

---

## T1498 — Network Denial of Service

### Description

Network Denial of Service represents adversary behavior intended to
prevent or degrade the availability of a targeted system or service
through network-based traffic.

### Evidence in This Project

The detection pipeline identified suspicious traffic using network
flow characteristics including:

- Flow packet rate
- Flow byte rate
- Flow duration
- Forward packet volume
- Backward packet volume
- Packet length

The dataset ground-truth labels identify the relevant attack traffic
as:

- DoS attacks-Hulk
- DoS attacks-SlowHTTPTest

---

## Detection Indicators

The project uses multiple network indicators to identify suspicious
traffic:

### High Packet Rate

Unusually high packets-per-second activity can indicate traffic
consistent with a denial-of-service pattern.

### High Byte Rate

Unusually high bytes-per-second activity can indicate high-volume
network traffic.

### Short Flow

Short-duration flows combined with other abnormal indicators can
increase suspicion.

### Abnormal Packet Volume

Unusual forward or backward packet counts can contribute to the
overall detection score.

### Large Packet Size

Unusually large average packet length can contribute to a
multi-indicator alert.

---

## Important Limitation

The available network-flow data does not by itself prove:

- attacker identity
- attacker intent
- command execution
- persistence
- credential theft
- malware execution
- account compromise

Therefore this project does not claim mappings for unrelated ATT&CK
techniques without supporting evidence.

The MITRE mapping represents behavioral alignment between the observed
network activity and Network Denial of Service (T1498).

---

## SOC L1 Investigation Usage

When an alert is associated with DoS-like behavior, an L1 analyst
should:

1. Validate the alert.
2. Review source and destination IP addresses.
3. Review destination port and protocol.
4. Check the event timestamp.
5. Examine traffic volume and flow characteristics.
6. Search for related events.
7. Determine whether the activity is expected or suspicious.
8. Document evidence.
9. Escalate confirmed or high-risk activity to L2.
10. Record the final disposition.

---

## Evidence Sources

Primary dataset:

CSE-CIC-IDS2018

Official dataset source:

https://registry.opendata.aws/cse-cic-ids2018/

Detection evidence:

- Detection Engine V2
- Detection evaluation
- SOC alert generation
- Root cause analysis
