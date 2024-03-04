from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Teleporte quântico
# Referência: https://qiskit.org/textbook/ch-algorithms/teleportation.html

# Definindo os registradores quânticos e clássicos
qr = QuantumRegister(3, name="q")  # Registradores quânticos
crz = ClassicalRegister(1, name="crz")  # Registrador clássico para a medição Z
crx = ClassicalRegister(1, name="crx")  # Registrador clássico para a medição X
teleportation_circuit = QuantumCircuit(qr, crz, crx)

# Preparação do estado inicial (Alice)
teleportation_circuit.h(1)
teleportation_circuit.cx(1, 2)

# Preparação do estado a ser teleportado (Bob)
teleportation_circuit.cx(0, 1)
teleportation_circuit.h(0)

# Medição do estado a ser teleportado e do qubit de Bell (Alice)
teleportation_circuit.measure(0, 0)
teleportation_circuit.measure(1, 1)

# Aplicação das correções de acordo com as medições (Bob)
teleportation_circuit.barrier(qr[1], qr[2])  # Barreira para sincronização
teleportation_circuit.z(2).c_if(crz, 1)  # Correção Z
teleportation_circuit.x(2).c_if(crx, 1)  # Correção X

# Visualização do circuito

imagem = teleportation_circuit.draw(output="mpl", style="iqx")
imagem.savefig("2.png")


