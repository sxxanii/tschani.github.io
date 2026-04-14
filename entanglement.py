from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

qc.h(0)          # put first qubit into superposition
qc.cx(0, 1)      # entangle qubit 1 with qubit 2

qc.measure([0, 1], [0, 1])

sim = AerSimulator()
result = sim.run(qc, shots=1000).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
plt.show()
