import cirq
from cirq.contrib.svg import circuit_to_svg

a, b = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.X(a), cirq.CNOT(a, b))

# Convertendo o circuito para SVG
svg_string = circuit_to_svg(circuit)

# Salvar o SVG em um arquivo
file_path = "circuit.svg"
with open(file_path, "w") as file:
    file.write(svg_string)
