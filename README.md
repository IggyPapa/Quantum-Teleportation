# Quantum Teleportation Simulator

Quantum teleportation transfers/teleports an exact quantum state from Alice to Bob without physically moving the qubit.
It requires both a quantum channel (the shared Bell pair) and a classical channel (Alice's 2 measurement bits) — neither alone is sufficient.

How it works
The circuit uses 3 qubits:

1) Alice's Message qubit which is initialized to a random state using a U gate with randomized angles θ, φ, and λ, simulating a random unknown quantum state
2) Alice's qubit which shares a Bell pair with Bob's qubit
3) Bob's qubit which as I previously mentioned shares a Bell pair with Alice's qubit

Alice performs a Bell State Measurement on her two qubits (a CNOT followed by a Hadamard) collapsing the system and producing 2 classical bits. 
These bits travel to Bob through a classical channel, and based on what he receives, Bob applies conditional Pauli corrections to recover Alice's exact original state.

For the verification the state fidelity is computed at the end by comparing Bob's final qubit against a reference statevector rebuilt from Alice's original angles. 
A fidelity of 1.0 confirms perfect teleportation.

Dependencies
python -m pip install numpy qiskit qiskit-aer sympy pylatexenc matplotlib
