"""
PyQubit v0.1

This module provides a simple and intuitive Python class for single-qubit
simulation. It is designed to be a foundational building block for a future
quantum computing library, allowing users to explore the fundamental
principles of quantum mechanics through code.

The main component is the `Qubit` class, which allows for state
initialization, application of common quantum gates, and measurement.
"""
import cmath
import math
import random
import secrets
import numpy as np

class Qubit:
    """
    A class to simulate a single quantum bit (qubit).

    This class represents a qubit's state as a 2D complex vector and provides
    methods to apply common quantum gates, perform measurements, and inspect
    its state.
    """
    def __init__(self, alpha, beta):
        """
        Initializes the qubit with a given state.

        The state is defined by two complex amplitudes, alpha and beta,
        for the |0> and |1> basis states, respectively. The state is
        automatically normalized upon initialization.

        Args:
            alpha (complex or float): The amplitude for the |0> state.
            beta (complex or float): The amplitude for the |1> state.
        """
        self.state = np.array([alpha, beta], dtype=complex)
        self.normalize()

    def normalize(self):
        """
        Ensures the qubit's state vector is a unit vector.

        This method calculates the norm of the state vector and divides
        each component by the norm, ensuring that the sum of the squared
        amplitudes is equal to 1.
        """
        norm = np.linalg.norm(self.state)
        if norm == 0:
            # Avoid division by zero, though this state is not physically valid
            return
        self.state = self.state / norm
    
    def apply_gate(self, gate_matrix):
        """
        Applies a given quantum gate to the qubit.

        Args:
            gate_matrix (np.ndarray): A 2x2 numpy array representing the
                                      quantum gate to be applied.

        Returns:
            Qubit: The Qubit object itself, allowing for method chaining.
        """
        self.state = np.dot(gate_matrix, self.state)
        self.normalize()
        return self
    
    def __str__(self):
        """
        Returns a string representation of the qubit's state.
        """
        return f"Qubit({self.state[0]}, {self.state[1]})"
    
    def measure(self):
        """
        Simulates a measurement of the qubit in the computational basis.

        The qubit's state collapses to either |0> or |1> based on the
        probabilities derived from its amplitudes.

        Returns:
            int: The measurement result (0 or 1).
        """
        prob_0 = abs(self.state[0])**2
        if secrets.randbelow(10**9) / 10**9 < prob_0:
            self.state = np.array([1, 0], dtype=complex)
            return 0
        else:
            self.state = np.array([0, 1], dtype=complex) 
            return 1
    
    # --- Single Qubit Gates ---

    def pauliX(self):
        """Applies the Pauli-X (NOT) gate."""
        m = np.array([[0, 1],[1, 0]], dtype=complex)
        return self.apply_gate(m)
    
    def pauliY(self):
        """Applies the Pauli-Y gate."""
        m = np.array([[0, -1j],[1j, 0]], dtype=complex)
        return self.apply_gate(m)
    
    def pauliZ(self):
        """Applies the Pauli-Z gate."""
        m = np.array([[1, 0],[0, -1]], dtype=complex)
        return self.apply_gate(m)
    
    def hadamard(self):
        """Applies the Hadamard gate."""
        m = (1/np.sqrt(2)) * np.array([[1, 1],[1, -1]], dtype=complex)
        return self.apply_gate(m)
    
    def phaseS(self):
        """Applies the Phase (S) gate."""
        m = np.array([[1, 0],[0, 1j]], dtype=complex)
        return self.apply_gate(m)
    
    def phaseT(self):
        """Applies the T gate (pi/8 gate)."""
        m = np.array([[1, 0],[0, cmath.exp(1j * np.pi / 4)]], dtype=complex)
        return self.apply_gate(m)
    
    # --- Rotation Gates ---

    def rX(self, theta):
        """
        Applies a rotation around the X-axis.

        Args:
            theta (float): The angle of rotation in radians.
        """
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        m = np.array([[c, -1j * s],
                      [-1j * s, c]], dtype=complex)
        return self.apply_gate(m)

    def rY(self, theta):
        """
        Applies a rotation around the Y-axis.

        Args:
            theta (float): The angle of rotation in radians.
        """
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        m = np.array([[c, -s],
                      [s, c]], dtype=complex)
        return self.apply_gate(m)

    def rZ(self, theta):
        """
        Applies a rotation around the Z-axis.

        Args:
            theta (float): The angle of rotation in radians.
        """
        m = np.array([[cmath.exp(-1j * theta / 2), 0],
                      [0, cmath.exp(1j * theta / 2)]], dtype=complex)
        return self.apply_gate(m)
    
    def probabilities(self):
        """
        Calculates the probabilities of measuring the qubit in the |0> and |1> states.

        Returns:
            np.ndarray: A numpy array containing the probabilities for
                        [P(|0>), P(|1>)].
        """
        return np.abs(self.state)**2
