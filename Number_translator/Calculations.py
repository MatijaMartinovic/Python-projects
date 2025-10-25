def combinations():
    number = "01"
    amount = []

    for a in number:
        for b in number:
            for c in number:
                nm = f"{a}{b}{c}"
                print(nm)
                amount.append(nm)

    print(f"Total combinations: {len(amount)}\nCalculated: {2**len(amount[0])}")


def calculate_bits():

    bit_number = input(str("Enter a binary number: "))

    sum = 0
    length = len(bit_number)
    for bit in bit_number:
        length -= 1
        if bit == "1":
            sum += (2**length)

    print(int(sum))

def dec_to_bin_short(dec_number):
    return str(bin(dec_number)[2:])

def dec_to_hex(dec):
    return str(hex(dec)[2:])

def dec_to_oct(dec):
    return str(oct(dec))[2:]

def dec_to_bin(dec_number:float) -> str:
    a = dec_number
    binary = ""

    while dec_number >= 1:
        if int(dec_number) % 2 == 0:
            binary += "0"
            dec_number /= 2
        else:
            binary += "1"
            dec_number /= 2
    
    print(f"Number {a} in binary is: {binary[::-1]}")
    return binary[::-1]




if __name__ == "__main__":
    print(dec_to_hex(15))
    print(dec_to_oct(15))