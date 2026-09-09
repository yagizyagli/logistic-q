# 🔌 Phase 2: Hybrid Classical-Quantum Cloud Integration

This document outlines the system architecture for connecting traditional Enterprise Resource Planning (ERP) systems and logistics databases with Cloud-native Quantum Computing Units (QPUs).

---

## 🏛️ 1. Co-Processing Architecture (The Hybrid Model)

Organizations cannot replace their entire IT stack with quantum computers. Instead, `logistic-q` enforces a **Hybrid Classical-Quantum Architecture**. 

Classical servers handle 95% of standard operations (Data storage, UI, basic filtering), while specific high-dimensional combinatorial problems are pushed asynchronously to a QPU.

```text
+-------------------+      Rest API / gRPC      +-----------------------+

|  Classical ERP    |  -----------------------> |   logistic-q Core     |
| (SAP/Oracle/Custom| <-----------------------  |  (Python Microservice)|
+-------------------+       JSON Payload        +-----------------------+
                                                            |
                                                            | Quantum API
                                                            v
                                                +-----------------------+

                                                |   Quantum Cloud Provider|
                                                | (D-Wave / AWS / IBM)  |
                                                +-----------------------+
```

---

## 🔄 2. The Execution Pipeline

Every optimization request processed by the framework follows a strict 4-step pipeline to maintain lightweight execution and high speed:

### Step 1: Ingestion & Serialization
The classical logistics engine packages routing requirements (nodes, fleet size, driver limits) into a standard JSON payload and sends it to the `logistic-q` API gateway.

### Step 2: Edge Pre-Processing
The framework strips unnecessary telemetry data, normalizes the distance matrix, and compiles the parameters into a QUBO (Quadratic Unconstrained Binary Optimization) structure using `core-poc/optimizer.py`.

### Step 3: QPU Dispatch (Asynchronous Task)
The normalized QUBO matrix is dispatched via secure API calls to a live Quantum Cloud platform. The process uses quantum annealing or gate-based QAOA to find the absolute minimum energy path.

### Step 4: Decryption & Classical Fallback
The returned quantum binary string is translated back into real-world geographic coordinates (Latitude/Longitude paths). 
*   **Safety net:** If the Quantum API times out (>5000ms), the system automatically triggers a **Classical Fallback** heuristic solver to prevent supply chain downtime.

---

## ☁️ 3. Supported Quantum Backends

`logistic-q` is built with abstraction layers, allowing seamless switching between different quantum infrastructure providers:

*   **D-Wave Leap (Recommended for Routing):** Excellent for immediate commercial use via Advantage Annealers, which handle up to 5000+ qubits for optimization tasks.
*   **AWS Braket (High Accessibility):** Aggregates multiple hardware providers (Rigetti, IonQ, D-Wave) under a single, unified AWS IAM security policy.
*   **IBM Quantum Runtime:** Optimized for gate-based quantum algorithms using primitives like Sampler and Estimator to execute fast variational loops.

---

## 🛠️ What's Next?
Connecting systems via APIs introduces security risks. Move to [Phase 3: Post-Quantum Cryptography & Supply Chain Security](./03_pqc_security.md) to understand how to safeguard logistics transport data against future quantum decryption threats.
