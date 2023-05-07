import numpy as np

# Define the Pauli X gate
X = np.array([[0, 1], [1, 0]])

# Define the Pauli Y gate
Y = np.array([[0, -1j], [1j, 0]])

# Define the Pauli Z gate
Z = np.array([[1, 0], [0, -1]])

# Define the Hadamard gate
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Define the CNOT gate
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# Define the input qubit states
q0 = np.array([1, 0])
q1 = np.array([0, 1])

# Apply the gates to the qubits
print("Applying gates to qubit state [1 0]:")
print("Pauli X gate: ", np.dot(X, q0))
print("Pauli Y gate: ", np.dot(Y, q0))
print("Pauli Z gate: ", np.dot(Z, q0))
print("Hadamard gate: ", np.dot(H, q0))
print("")

print("Applying gates to qubit state [0 1]:")
print("Pauli X gate: ", np.dot(X, q1))
print("Pauli Y gate: ", np.dot(Y, q1))
print("Pauli Z gate: ", np.dot(Z, q1))
print("Hadamard gate: ", np.dot(H, q1))
print("")

print("Applying CNOT gate to qubit states [1 0] and [0 1]:")
q0q1 = np.kron(q0, q1)
print("Before CNOT: ", q0q1)
q0q1 = np.dot(CNOT, q0q1)
print("After CNOT: ", q0q1)
