# 📝 Quantum Readiness Assessment Survey

This lightweight questionnaire is designed for logistics enterprises to evaluate their current technological infrastructure and data architecture before integrating the `logistic-q` engine.

---

## 💻 Section 1: Classical Computational Bottlenecks
1. What is the average computation time required to generate daily vehicle routing and scheduling schedules?
   * [ ] Less than 15 minutes
   * [ ] 15 to 60 minutes
   * [ ] 1 to 4 hours
   * [ ] More than 4 hours (High Quantum Suitability)

2. How often do real-time disruptions (e.g., weather, traffic, fleet breakdown) force your system to recalculate routes midday?
   * [ ] Rarely / Scheduled once a day
   * [ ] Occasionally (1-2 times a day)
   * [ ] Continuously / Real-time updates required (High Quantum Suitability)

---

## 🗄️ Section 2: Data & ERP Infrastructure
3. Which core Enterprise Resource Planning (ERP) or Supply Chain Management (SCM) system does your organization use?
   * [ ] SAP S/4HANA / Oracle SCM
   * [ ] Proprietary / Custom-built in-house software
   * [ ] Legacy relational databases (SQL Server, Oracle DB) without modern API endpoints

4. Does your logistics pipeline expose telemetry and coordinate matrices via standard REST or gRPC APIs?
   * [ ] Yes, fully modernized
   * [ ] Partially, requires custom middleware wrappers
   * [ ] No, data pipeline is batch-processed manually

---

## 🔒 Section 3: Cyber Security & Cryptography
5. What is the current public-key encryption standard securing your primary logistics databases and cloud communications?
   * [ ] RSA-2048 / RSA-4096
   * [ ] ECC (Elliptic Curve Cryptography)
   * [ ] Unsure / Legacy infrastructure

6. Does your corporate security compliance roadmap include provisions for Post-Quantum Cryptography (PQC) or NIST compliance timelines?
   * [ ] Yes, active transition planning is underway
   * [ ] No, not currently on our near-term timeline
