# PyQubit v0.3.1 (first version)
<p align="center">
  <img src="LOGO.svg" alt="PyQubit logo" height="100"/>
</p>


[![PyPI version](https://img.shields.io/pypi/v/pyqubit.svg)](https://pypi.org/project/pyqubit/)
[![Python Version](https://img.shields.io/pypi/pyversions/pyqubit.svg)](https://pypi.org/project/pyqubit/)
[![Downloads](https://pepy.tech/badge/pyqubit)](https://pepy.tech/project/pyqubit)


A simple and intuitive Python class for single-qubit simulation.

---

## Installation

```bash
pip install pyqubit
```

## Quick Start

```python
from pyqubit import Qubit

q = Qubit(1, 0)
print(q)
q.hadamard()
print(q.probabilities())
```

---

## ✨ Features

- **Qubit State Management**: Initialize a qubit in any valid superposition of the ∣0⟩ and ∣1⟩ states.
- **State Normalization**: Automatically ensures the qubit's state vector remains valid after every operation.
- **Measurement Simulation**: Collapse the qubit's state to a classical bit (0 or 1) based on its quantum probabilities.
- **Standard Single-Qubit Gates**:
  - Pauli-X (NOT)
  - Pauli-Y
  - Pauli-Z
  - Hadamard
  - Phase (S)
  - Phase (T)
- **Parametrized Rotation Gates**:
  - Rotation around X-axis (`rX`)
  - Rotation around Y-axis (`rY`)
  - Rotation around Z-axis (`rZ`)
- **Probability Inspection**: Easily retrieve the probabilities of measuring the qubit in the ∣0⟩ or ∣1⟩ state.

---
## v/s Qiskit
<img width="775" height="281" alt="image" src="https://github.com/user-attachments/assets/e8762b75-fe3e-4057-a4eb-17c89b42f770" />



## 🧩 Installation



```bash

pip install pyqubit
```

---

## 🚀 Usage Guide

### 1. Import the Class

Save the file as `qubit.py`, then:

```python
from qubit import Qubit
import numpy as np
```

---

### 2. Initializing a Qubit

```python
# Create a qubit in the state |0⟩ (alpha=1, beta=0)
q = Qubit(1, 0)
print(f"Initial state: {q}")
# Output: Qubit((1+0j), (0+0j))
```

---

### 3. Applying Gates

#### Hadamard Gate – Creating Superposition

```python
q = Qubit(1, 0)      # Start in |0⟩
q.hadamard()
print(f"State after Hadamard: {q}")

probs = q.probabilities()
print(f"Probabilities: P(|0⟩)={probs[0]:.1%}, P(|1⟩)={probs[1]:.1%}")
```

#### Pauli-X (NOT) Gate

```python
q = Qubit(1, 0)
print(f"Before Pauli-X: {q}")

q.pauliX()
print(f"After Pauli-X: {q}")
```

---

### 4. Performing a Measurement

```python
q = Qubit(1, 1)  # Automatically normalized to superposition
print(f"Superposition: {q}")

print("Performing 10 measurements...")
for _ in range(10):
    result = q.measure()
    print(f"Measured: {result}, Collapsed state: {q}")
```

---

### 5. Applying Rotation Gates

```python
q = Qubit(1, 0)

# Rotate by 90° (π/2 radians) around Y-axis
q.rY(np.pi / 2)
print(f"After rY(π/2): {q}")
print(f"Probabilities: {q.probabilities()}")
```

---

## 🔭 Future Plans (v0.2+)

* **Multi-Qubit Systems**: Add `QuantumRegister` to manage multiple qubits.
* **Entanglement Support**: Add CNOT, Toffoli, and other multi-qubit gates.
* **Quantum Circuits**: Circuit builder and execution.
* **Performance Boosts**: Optimized calculations for larger systems.
* **Visualization**: Bloch sphere and state vector plotting tools.

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE). 
