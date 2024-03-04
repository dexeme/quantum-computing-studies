import cirq
from cirq.contrib.svg import circuit_to_svg
import numpy as np

def make_quantum_teleportation_circuit(gate):
    """Retorna um circuito para teletransporte quântico.

    Este circuito 'teletransporta' um estado de qubit aleatório preparado pelo
    portão de entrada de Alice para Bob.
    """
    circuit = cirq.Circuit()

    # Obtenha os três qubits envolvidos no protocolo de teletransporte.
    msg = cirq.NamedQubit("Mensagem")
    alice = cirq.NamedQubit("Alice")
    bob = cirq.NamedQubit("Bob")

    # O portão de entrada prepara a mensagem para enviar.
    circuit.append(gate(msg))

    # Crie um estado Bell compartilhado entre Alice e Bob.
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])

    # Medição de Bell da Mensagem e do qubit entrelaçado de Alice.
    circuit.append([cirq.CNOT(msg, alice), cirq.H(msg), cirq.measure(msg, alice)])

    # Usa os dois bits clássicos da medição de Bell para recuperar a
    # mensagem quântica original no qubit entrelaçado de Bob.
    circuit.append([cirq.CNOT(alice, bob), cirq.CZ(msg, bob)])

    return circuit

# Crie um circuito para teletransporte quântico com um portão de entrada aleatório.
circuit = make_quantum_teleportation_circuit(cirq.X)

"""Visualize o circuito de teletransporte."""
# Portão para colocar o qubit da mensagem em algum estado para enviar.
gate = cirq.X ** 0.25

# Crie o circuito de teletransporte.
circuit = make_quantum_teleportation_circuit(gate)
print("Circuito de teletransporte:\n")
print(circuit)

"""Exiba o vetor de Bloch do qubit da mensagem."""
message = cirq.Circuit(gate.on(cirq.NamedQubit("Mensagem"))).final_state_vector()
message_bloch_vector = cirq.bloch_vector_from_state_vector(message, index=0)
print('\n')
print("Vetor de Bloch do qubit da mensagem:")
print(np.round(message_bloch_vector, 3))

# Convertendo o circuito para SVG
svg_string = circuit_to_svg(circuit)

# Salvar o SVG em um arquivo
file_path = "circuit.svg"
with open(file_path, "w") as file:
    file.write(svg_string)
