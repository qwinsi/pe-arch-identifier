# Identify the architecture of PE file (x86, x86_64, ARM64 or other)

import sys
import pefile

def main():
    if len(sys.argv) != 2:
        print("Usage: pe_arch.py <file>")
        sys.exit(1)

    try:
        pe = pefile.PE(sys.argv[1])
        if pe.FILE_HEADER.Machine == 0x014c:
            print("x86 32-bit")
        elif pe.FILE_HEADER.Machine == 0x8664:
            print("x86_64")
        elif pe.FILE_HEADER.Machine == 0xAA64:
            print("ARM64")
        else:
            print("Other machine type: {}".format(pefile.MACHINE_TYPE[pe.FILE_HEADER.Machine]))
    except pefile.PEFormatError as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
