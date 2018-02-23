from qiskit import QuantumProgram
import Qconfig

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set APIToken and API URL

# setup registers and program
qr = qp.create_quantum_register('qr', 16)
cr = qp.create_classical_register('cr', 16)
qc = qp.create_circuit('smiley_writer', [qr], [cr])

# rightmost eight (qu)bits have ')' = 00101001
qc.x(qr[0])
qc.x(qr[3])
qc.x(qr[5])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[9]) # create superposition on 9
qc.cx(qr[9],qr[8]) # spread it to 8 with a cnot
qc.x(qr[11])
qc.x(qr[12])
qc.x(qr[13])
qc.barrier(qr) # required for qiskit turtorial issue #88 workaround

# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run and get results
results = qp.execute(["smiley_writer"], backend='ibmqx_qasm_simulator', shots=1024)
stats = results.get_counts("smiley_writer")

for i in iter(stats):
    prob = (stats.get(i) / 1024) * 100
    char1 = chr(int(i[0:8],2))
    char2 = chr(int(i[9:16],2))

    print('{0}{1} - {2}%'.format(char1,char2,prob))
