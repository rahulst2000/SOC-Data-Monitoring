# SOC L1 Incident Investigation Report

## 1. Incident Overview

**Project:** Security Data Monitoring & SOC Investigation Platform  
**Dataset:** CSE-CIC-IDS2018  
**Investigation Level:** SOC L1  
**Analysis Type:** Network Traffic / DoS Detection  
**Detection Engine:** Detection Engine V2

### Incident Category

Network Denial of Service (DoS)

### Dataset Attack Types

- DoS attacks-Hulk
- DoS attacks-SlowHTTPTest

---

# 2. Detection Summary

The detection engine analyzed:

**900,988 network-flow records**

Detection Engine V2 generated:

**29,640 suspicious records**

Offline ground-truth evaluation identified:

- True Positives: 27,279
- False Positives: 2,361
- Precision: 92.03%

The evaluation indicates that the detector successfully identified
many records associated with the known attack traffic, while also
generating benign-traffic alerts that require L1 validation.

---

# 3. Detection Indicators

Detection Engine V2 evaluates multiple network-flow indicators.

### High Packet Rate

Unusually high packets-per-second activity.

### High Byte Rate

Unusually high bytes-per-second activity.

### Short Flow

Short-duration network flows combined with other indicators.

### High Forward Packet Volume

Unusually high forward packet counts.

### High Backward Packet Volume

Unusually high backward packet counts.

### Large Packet

Unusually large average packet length.

---

# 4. Alert Generation

An alert is generated when multiple detection indicators are
triggered.

The detection engine calculates an indicator count and converts
that count into a risk score.

Risk scoring:

| Indicator Count | Risk Score |
|---:|---:|
| 0 | 0 |
| 1 | 20 |
| 2 | 40 |
| 3 | 60 |
| 4 | 80 |
| 5 | 100 |
| 6 | 100 |

A record with at least two indicators is classified as:

**SUSPICIOUS**

---

# 5. Alert Distribution

Detection Engine V2 produced:

| Detection Type | Alerts |
|---|---:|
| HIGH_PACKET_RATE, SHORT_FLOW | 22,748 |
| HIGH_BYTE_RATE, SHORT_FLOW | 4,555 |
| HIGH_BACKWARD_PACKETS, LARGE_PACKET | 2,161 |
| HIGH_FORWARD_PACKETS, HIGH_BACKWARD_PACKETS | 99 |
| HIGH_FORWARD_PACKETS, LARGE_PACKET | 40 |
| HIGH_BYTE_RATE, SHORT_FLOW, LARGE_PACKET | 30 |
| HIGH_BYTE_RATE, HIGH_FORWARD_PACKETS, HIGH_BACKWARD_PACKETS, LARGE_PACKET | 4 |
| HIGH_PACKET_RATE, HIGH_BYTE_RATE, SHORT_FLOW | 2 |
| HIGH_FORWARD_PACKETS, HIGH_BACKWARD_PACKETS, LARGE_PACKET | 1 |

---

# 6. Ground-Truth Validation

Among the 29,640 suspicious records:

| Classification | Records |
|---|---:|
| DoS attacks-SlowHTTPTest | 19,462 |
| DoS attacks-Hulk | 7,817 |
| Benign | 2,361 |
| **Total** | **29,640** |

The 2,361 benign records are treated as:

**False Positive Candidates**

They require contextual validation before an analyst closes the alert.

---

# 7. SOC L1 Investigation Process

For a suspicious network-flow alert, the L1 analyst should:

1. Validate the alert.
2. Identify source IP.
3. Identify destination IP.
4. Review destination port.
5. Review protocol.
6. Review timestamp.
7. Review traffic characteristics.
8. Check whether similar events occurred around the same time.
9. Determine whether the traffic is expected.
10. Check available threat intelligence or organizational context.
11. Assign severity.
12. Document evidence.
13. Contain or escalate according to the organization's playbook.

---

# 8. Evidence to Collect

The following information should be collected during investigation:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Protocol
- Timestamp
- Flow duration
- Packet rate
- Byte rate
- Forward packet count
- Backward packet count
- Average packet length
- Detection indicators
- Risk score
- Related alerts
- Host or asset information when available

---

# 9. Severity Assessment

### Critical

Use when:

- High-confidence malicious traffic is identified.
- The target is a critical asset.
- Traffic volume indicates significant availability impact.
- Multiple related indicators or alerts exist.

**L1 Action:** Immediate escalation to L2 and follow containment procedures.

### High

Use when:

- Strong evidence of malicious DoS activity exists.
- Multiple detection indicators are present.
- The target appears to be under sustained attack.

**L1 Action:** Investigate immediately and escalate according to the SOC procedure.

### Medium

Use when:

- Suspicious traffic is detected but malicious activity is not yet
  confirmed.
- Additional contextual validation is required.

**L1 Action:** Investigate related events and validate the activity.

### Low

Use when:

- An alert has weak evidence.
- The activity appears operational or expected.

**L1 Action:** Validate and monitor.

---

# 10. Root Cause Analysis

The project identified that statistical network-flow thresholds can
generate alerts for both malicious and benign traffic.

The root-cause analysis therefore distinguishes between:

### Confirmed Dataset Attack Traffic

Traffic labeled by the dataset as:

- DoS attacks-Hulk
- DoS attacks-SlowHTTPTest

### False Positive Candidates

Traffic that triggered the detection rules but has a dataset label of:

**Benign**

These records should not automatically be considered malicious.

An L1 analyst should validate the surrounding context before
closing the alert.

---

# 11. MITRE ATT&CK Mapping

The observed DoS behavior is mapped behaviorally to:

**T1498 — Network Denial of Service**

The available network-flow evidence does not independently establish:

- Attacker identity
- Attacker intent
- Persistence
- Credential theft
- Malware execution
- Account compromise

Therefore, unrelated ATT&CK techniques are not claimed without
supporting evidence.

---

# 12. L1 Disposition

### Attack-Matching Alert

**Disposition: ESCALATE_TO_L2**

Recommended action:

- Preserve evidence.
- Review related traffic.
- Identify affected assets.
- Check for continued activity.
- Escalate confirmed/high-confidence incidents.

### Benign Alert

**Disposition: FALSE_POSITIVE_CANDIDATE**

Recommended action:

- Validate application context.
- Check whether traffic is expected.
- Search for related events.
- Document the reason for closure if confirmed benign.

---

# 13. Containment Recommendations

If a DoS attack is confirmed in a real environment, possible
containment actions include:

- Apply appropriate network filtering.
- Rate-limit abusive traffic.
- Block malicious sources when justified.
- Protect affected services using firewall or DDoS controls.
- Coordinate with network/security teams.
- Preserve relevant logs and evidence.
- Monitor for continued attack activity.

Containment actions must follow the organization's approved
incident-response procedures.

---

# 14. Detection Performance

The initial threshold experiments demonstrated very high precision
but poor recall.

Detection Engine V2 improved the alert-selection approach and
produced:

**29,640 suspicious records**

Offline evaluation of these alerts produced:

**92.03% precision**

However, this project should not claim that the detector catches all
attacks. The overall dataset contains 454,335 attack records, while
27,279 attack records were selected by V2.

This demonstrates an important detection-engineering lesson:

> High precision does not automatically mean high detection coverage.

Further tuning and additional detection logic would be required for
production deployment.

---

# 15. Analyst Conclusion

The investigation demonstrates a complete SOC L1 workflow:

**Network Data → Validation → Detection → Alert → Investigation →
Ground-Truth Validation → Root Cause Analysis → MITRE Mapping →
Disposition → Escalation**

The project also demonstrates the importance of false-positive
analysis and detection-rule evaluation.

The detection engine should be considered a research/lab detection
system and not a production security control without additional
validation, tuning, and real-environment testing.

---

# 16. Project Evidence

Key project components:

- Data validation
- Data profiling
- Data cleaning
- Security traffic analysis
- Feature baseline analysis
- Threat detection
- Detection rule evaluation
- Detection tuning
- Detection Engine V2
- Alert generation
- Root cause analysis
- MITRE ATT&CK mapping
- SOC L1 incident investigation

---

## Dataset

CSE-CIC-IDS2018

Official source:

https://registry.opendata.aws/cse-cic-ids2018/
