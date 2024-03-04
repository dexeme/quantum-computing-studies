import cirq
from cirq.contrib.svg import circuit_to_svg

a, b, c = cirq.LineQubit.range(3)
circuit = cirq.Circuit(
    cirq.H(a),
    cirq.CNOT(a, b),
    cirq.CNOT(b, c),
    cirq.X(a),
    cirq.Y(b),
    cirq.Z(c),
    cirq.measure(a, b, c)
)

# Convertendo o circuito para SVG
svg_string = circuit_to_svg(circuit)

# Salvar o SVG em um arquivo
file_path = "circuit.svg"
with open(file_path, "w") as file:
    file.write(svg_string)
