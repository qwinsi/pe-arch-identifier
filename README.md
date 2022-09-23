# PE Architecture Identifier

This is a simple python script to identify the architecture of a PE file (x86, x86_64, ARM64 or other).

## Usage

```shell
python pe_arch.py <path to PE file>
```

## Example

```shell
$ python pe_arch.py samples/example-i386.exe
Machine type: x86 32-bit
$ python pe_arch.py samples/example-amd64.exe
Machine type: x86_64
$ python pe_arch.py samples/example-arm64.exe
Machine type: ARM64
```

## Dependencies

- [pefile](https://pypi.org/project/pefile/)

```shell
pip install pefile
```
