# Integrated Vulnerability Prioritization Using CVSS, EPSS and ATT&CK 

##  Methodology: 
  The methodology outlined below presents a systematic, multi-stage approach 
designed to enhance vulnerability prioritization by integrating three critical 
dimensions of cyber risk: severity (CVSS), exploitability (EPSS), and adversary 
behavior (MITRE ATT&CK). Each step contributes to the development of a unified 
scoring framework that reflects both technical impact and real-world threat relevance, 
thereby enabling more informed and effective remediation strategies. 
## a) Collect Data:
  Collect CVE data from NVD, exploit likelihood from EPSS, 
  and attack technique info from MITRE ATT&CK. 
## b) Clean & Prepare:
  Organize CVEs, remove duplicates, and handle missing 
  values 
## c) Predict Missing CVSS: 
  Use machine learning to fill in missing CVSS values 
  so that every CVE has a complete severity score. 
## d) Merge EPSS & ATT&CK: 
  Add exploit probability (EPSS) and known 
  attacker techniques (ATT&CK) to each CVE. 
## e) Build Composite Score (PSSS): 
  Combine CVSS (severity), EPSS (exploitability), and ATT&CK (attacker relevance) into one unified score. 
## f) Rank Vulnerabilities: 
  Sort CVEs by the new score so that the most dangerous and likely-to-be-exploited ones appear at the top. 
## End result: A prioritization system that helps security teams focus on the riskiest vulnerabilities first. 
