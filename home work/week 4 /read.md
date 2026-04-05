# Blue Team — Detecting & Managing Scan Noise

When someone scans you, the artifacts appear across **multiple telemetry layers**:

|Layer|Where scan noise appears|
|---|---|
|Network|Firewall, IDS/IPS, NetFlow|
|Host|OS logs, service logs|
|Application|Web server logs|
|SIEM|Correlation of all signals|

A blue team does **three things**: detect → classify → respond.

---

## 1️ Detection Techniques

### A. Firewall / Network Device Detection

Typical scan patterns:

|Scan type|Log indicator|
|---|---|
|TCP SYN scan|Many SYN packets, few completed handshakes|
|Full connect scan|Many short-lived connections|
|UDP scan|Many ICMP Port Unreachable replies|
|Stealth scan|Incomplete/invalid TCP flags|

Example detection rule logic:

```
IF source_ip connects to >100 ports within 60 seconds
THEN flag as port scan
```

This is implemented using:

- Rate-based alerts
    
- Connection threshold alerts
    

---

### B. IDS/IPS Signatures

IDS engines detect **scan fingerprints**:

Indicators:

- Sequential port access (1,2,3,4…)
    
- Same packet size repeated
    
- Same TCP window size
    
- Same TTL values
    
- Same inter-packet timing
    

This creates a **scanner fingerprint**.

---

### C. Behavioral Analytics (SIEM)

Modern SOCs detect scanning via **behavior**, not just signatures:

Example correlation:

```
Single IP →
  hits many ports →
  hits many hosts →
  fails authentication →
  triggers geo anomaly
```

This becomes **reconnaissance activity**.

---

## Response & Mitigation

### A. Automatic Blocking

Blue team tools will:

- Rate limit connections
    
- Temporarily block IP
    
- Geo-block regions
    
- Add IP to threat intel feeds
    

Typical response timeline:

|Time|Action|
|---|---|
|Seconds|IDS alert|
|Minutes|Firewall block|
|Hours|Threat intel sharing|

---

### B. Deception Techniques (Advanced)

Mature blue teams deploy **honeypots / tarpit systems**.

When scanner detected:

- Redirect attacker to fake services
    
- Slow responses dramatically
    
- Feed fake banners
    
- Waste attacker time
    

This is called **active defense / deception**.

---

#  Red Team — Reducing Scan Noise

Red team goal = **avoid detection thresholds**.

Not “be invisible” — just stay **below alerting thresholds**.

This is called:

> Low-and-slow reconnaissance

---

## 1️ Timing Evasion (MOST IMPORTANT)

Fast scans trigger rate alerts.

Noisy scan:

```
1000 ports in 1 second → ALERT
```

Stealth scan:

```
1 port every 30 seconds → looks like normal traffic
```

This defeats:

- Rate-based IDS
    
- Firewall thresholds
    
- SIEM correlation windows
    

This is called **slow scanning**.

---

## 2️Randomization

Detection loves patterns.

Bad:

```
1,2,3,4,5,6,7,8...
```

Stealth:

```
443 → 22 → 8080 → 53 → 3389 → random order
```

Breaks signature detection.

---

## 3️ Distributed Scanning

Instead of:

```
1 IP scanning 1000 ports
```

Use:

```
100 IPs scanning 10 ports each
```

Now no single source crosses thresholds.

This defeats:

- Source-based detection
    
- Rate limits
    
- IP blocking
    

---

## 4️ Scan Only High-Value Ports

Real attackers rarely scan all 65535 ports.

They scan:

```
21,22,23,25,53,80,110,139,443,445,3389,8080
```

Why?

Because scanning all ports screams **scanner**.

Targeted scanning looks like **normal user traffic**.

---

## 5️ Blend With Legitimate Traffic

Example:

- Scan port 443 slowly
    
- Perform real TLS handshake
    
- Fetch real webpage
    

Now traffic looks like a browser, not a scanner.

This defeats:

- DPI inspection
    
- Behavior analytics
    

---

## 6️ Use Indirect Reconnaissance

Best red teamers avoid touching the target at all initially.

They gather data via:

|Technique|Noise level|
|---|---|
|DNS enumeration|None|
|Certificate transparency logs|None|
|Shodan/Censys search|None|
|Passive OSINT|None|

This is called **passive reconnaissance**.

Zero logs on target.

---

