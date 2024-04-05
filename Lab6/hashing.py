# 2 вариант (умножение, CRC-16)
import math


def mult_hash(text, m=2**10):
    """Хэширование через умножение"""
    const = (math.sqrt(5) - 1) / 2
    codes = [int(m * ((ord(letter) * const) % 1)) for letter in text]
    return codes


def reverse_poly(poly):
    return int(f"{poly:016b}"[::-1], 2)


def crc_16(text, start_crc, polynom, xor_out):
    """Хэширование методом CRC-16 с LSB"""
    data = bytearray(bytes(text, "utf-8"))
    crc = reverse_poly(start_crc)
    polynom = reverse_poly(polynom) 
    for elem in data:
        crc ^= elem
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ polynom
            else:
                crc = (crc >> 1)
    return crc ^ xor_out


if __name__ == "__main__":
    s = input("Введите строку для вычисления CRC:\n")
    # CRC-16/ARC
    print("CRC-16/ARC", hex(crc_16(s, polynom=0x8005, start_crc=0x0000, xor_out=0x0000)))
    # CRC-16/DNP
    print("CRC-16/DNP", hex(crc_16(s, polynom=0x3D65, start_crc=0x0000, xor_out=0xFFFF)))
    # CRC-16/KERMIT
    print("CRC-16/KERMIT", hex(crc_16(s, polynom=0x1021, start_crc=0x0000, xor_out=0x0000)))
    # CRC-16/MAXIM
    print("CRC-16/MAXIM", hex(crc_16(s, polynom=0x8005, start_crc=0x0000, xor_out=0xFFFF)))
    # CRC-16/MCRF4XX
    print("CRC-16/MCRF4XX", hex(crc_16(s, polynom=0x1021, start_crc=0xFFFF, xor_out=0x0000)))
    # CRC-16/USB
    print("CRC-16/USB", hex(crc_16(s, polynom=0x8005, start_crc=0xFFFF, xor_out=0xFFFF)))