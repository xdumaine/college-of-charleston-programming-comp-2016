def isXor(gate1, gate2):
    return (gate1 == 'T' and gate2 == 'F') or (gate1 == 'F' and gate2 == 'T')

gates = int(input())
while gates != 0:
    gatesOutput = []
    for x in range(0, gates):
        gatesOutput.append(0)
    for x in range(0, gates):
        gate = str(raw_input()).split(' ')
        gateNum = int(gate[0])
        gate1 = gate[1]
        gate2 = gate[2]
        if gate1 != 'T' and gate1 != 'F':
            gate1 = gatesOutput[int(gate1)]
        if gate2 != 'T' and gate2 != 'F':
            gate2 = gatesOutput[int(gate2)]
        if isXor(gate1, gate2):
            gatesOutput[gateNum] = 'T'
        else:
            gatesOutput[gateNum] = 'F'

    print gatesOutput[gates-1]

    gates = int(input())
