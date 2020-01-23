import null as null


class Number:
    decimal = 0
    binary = 0
    hexNum = 0

    def __init__(self, v):
        if "x" in v:
            self.hexNum = v
            self.decimal = int(v, 0)
            self.binary = bin(self.decimal)
        elif "b" in v or "B" in v:
            if v[0:1] != "0":
                v = "0" + v
            self.binary = v
            self.decimal = int(self.binary, 2)
            self.hexNum = hex(int(self.binary, 2))
        else:
            self.decimal = int(v)
            self.binary = bin(int(v))
            self.hexNum = hex(int(v))

    def toString(self):
        return str(self.decimal) + "    " + str(self.hexNum) + "    " + str(self.binary)

    def getbinary(self):
        return self.binary[2:]

    def getdecimal(self):
        return self.decimal


def andop(num1, num2):
    output = ""
    count = 0
    lendiff = max(len(num1), len(num2)) - min(len(num1), len(num2))
    if lendiff != 0:
        if len(num1) < len(num2):
            for x in range (0, lendiff):
                num1 = "0" + num1
        elif len(num2) < len(num1):
            for x in range (0, lendiff):
                num2 = "0" + num2
    while count < min(len(num1), len(num2)):
        if num1[count] == "1" and num2[count] == "1":
            output += "1"
        else:
            output += "0"
        count += 1
    return output


def orop(num1, num2):
    output = ""
    count = 0
    lendiff = max(len(num1), len(num2)) - min(len(num1), len(num2))
    if lendiff != 0:
        if len(num1) < len(num2):
            for x in range(0, lendiff):
                num1 = "0" + num1
        elif len(num2) < len(num1):
            for x in range(0, lendiff):
                num2 = "0" + num2
    while count < len(num1):
        if num1[count] == "1" or num2[count] == "1":
            output += "1"
        else:
            output += "0"
        count += 1
    return output


def xorop(num1, num2):
    output = ""
    count = 0
    lendiff = max(len(num1), len(num2)) - min(len(num1), len(num2))
    if lendiff != 0:
        if len(num1) < len(num2):
            for x in range(0, lendiff):
                num1 = "0" + num1
        elif len(num2) < len(num1):
            for x in range(0, lendiff):
                num2 = "0" + num2
    while count < len(num1):
        if num1[count] != num2[count]:
            output += "1"
        else:
            output += "0"
        count += 1
    return output


def leftshift(num1, num2):
    output = num1
    count = 0
    maxreps = int(num2)
    while count < maxreps:
        output += "0"
        count += 1
    return output


def rightshift(num1, num2):
    output = num1
    count = 0
    while count < int(num2):
        output = output[0:len(output) - 1]
        count += 1
    return output


def notop(num):
    output = ""
    count = 0
    while count < len(num):
        if num[count] == "1":
            output += "0"
        elif num[count] == "0":
            output += "1"
        count += 1
    return output


def andnot(num1, num2):
    lendiff = max(len(num1), len(num2)) - min(len(num1), len(num2))
    if lendiff != 0:
        if len(num1) < len(num2):
            for x in range(0, lendiff):
                num1 = "0" + num1
        elif len(num2) < len(num1):
            for x in range(0, lendiff):
                num2 = "0" + num2
    return andop(num1, notop(num2))


while True:
    print("When entering numbers, you can enter:")
    print("     A normal decimal integer number as big as 2^{64}-1.")
    print("     An integer number in hex up to 16 digits, starting with 0x.")
    print("     An integer number in binary up to 64 digits, starting with 0b.")
    print("Enter a problem: number AND|OR|XOR|LS|RS|ANDNOT number:")

    try:
        inputStr = input()
    except EOFError:
        exit()

    numberC = null
    operation = ""

    for elem in inputStr:
        if elem == "A" or elem == "N" or elem == "D" or \
                elem == "X" or elem == "O" or elem == "R" or \
                elem == "L" or elem == "S" or elem == "T":
            operation += elem
    operation = operation.strip()

    if len(inputStr.split()) != 3:
        print("Must provide 3 inputs")
        continue

    if operation != "AND" and operation != "OR" and operation != "XOR" and operation != "LS" and operation != "RS" and operation != "ANDNOT":
        print("Operation is not valid")
        continue

    try:
        numberA = Number(inputStr.split(operation)[0].strip())
        numberB = Number(inputStr.split(operation)[1].strip())
    except (ValueError):
        print("Input numbers should be decimal, binary, or hex")
        continue

    binA = numberA.getbinary()
    binB = numberB.getbinary()
    decA = numberA.getdecimal()
    decB = numberB.getdecimal()

    if operation == "AND":
        numberC = Number("0b" + andop(numberA.getbinary(), numberB.getbinary()))
    elif operation == "OR":
        numberC = Number("0b" + orop(numberA.getbinary(), numberB.getbinary()))
    elif operation == "XOR":
        numberC = Number("0b" + xorop(numberA.getbinary(), numberB.getbinary()))
    elif operation == "LS":
        numberC = Number("0b" + leftshift(binA, decB))
    elif operation == "RS":
        numberC = Number("0b" + rightshift(binA, decB))
    elif operation == "ANDNOT":
        numberC = Number("0b" + andnot(numberA.getbinary(), numberB.getbinary()))

    # output
    print("\nCompute Result:")
    print("     Operation: ", operation)
    print("     A: ", numberA.toString())
    print("     B: ", numberB.toString())
    print("     C: ", numberC.toString())
