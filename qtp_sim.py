import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector, state_fidelity
import matplotlib.pyplot as plt

qr = QuantumRegister(3) # quantum register that holds 3 qubits
#qr[0] is the qubits that Alice wants to teleport (message qubit)
#qr[1] is Aliec's entangled qubit
#qr[2] is Bob's entangled qubit
cr = ClassicalRegister(2)
# the classical register where the information is stored post measurment

qc = QuantumCircuit(qr, cr)

#using random angles to simulate alice having a random quantum state
theta = np.random.uniform(0, np.pi) 
phi = np.random.uniform(0, 2 * np.pi)
lam = np.random.uniform(0, 2 * np.pi)

qc.u(theta, phi, lam, qr[0])

qc.h(qr[1])
qc.cx(qr[1], qr[2])
# this puts q1 & q2 in a |Φ+> Bell state 
# note that the kind of Bell state doesn't matter 
# look at personal notes for the math proof

qc.cx(qr[0], qr[1])
qc.h(qr[0]) 
# this is what the prof called an inverse bell circuit

qc.measure(qr[0], cr[0])
# this measures q0 annd stores the result in the classical register we created before
qc.measure(qr[1], cr[1])
# same logic

qc.barrier()

with qc.if_test((cr[1], 1)):
    qc.x(qr[2])

with qc.if_test((cr[0], 1)):
    qc.z(qr[2])
# Bob corrects his qubits based on the infromation he got
# note : for the case where cr[0] = 1 and cr[1] = 1 you can not use the y gate because Y = iXZ
# if you want to see the logic go to personal notes (notebook 1) Quantum Teleportation page 7

original = QuantumCircuit(1)
# Creating a neew clean circuit to store the original state 
# and compare it with the state that bob got after the correction
# so w ecan see whether or not the teleportation was successful
original.u(theta, phi, lam, 0)
# note : the reason we use 0 instead of something like qr[0] like we did before is 
# because when we created the new cicuit we made it with 1 qubit, and because we didn't give it a 
# specific name Qiskit automatically referes to it as 0
a_state = Statevector.from_instruction(original)
# this extracts the state from the circuit as a math state that we can work with

print(f"Alice's original state: {a_state.draw('latex_source')}")
print(f"Angles — θ: {theta:.4f}, φ: {phi:.4f}, λ: {lam:.4f}")

qc.draw("mpl", 
        fold=-1,                  # This keeps the circuit in one continuous line
        scale=0.6,                # Shrinks the qubits so more can fit on screen
        style={'figsize': (50, 15),
               'fontsize': 8},    
               # this makes the tect smaller so it's more readable
        plot_barriers=True)
plt.show();
