# PE Architecture Identifier

This is a simple python script to identify the architecture of a PE file (x86, x86_64, ARM64 or other).

## Usage

```shell
python pe_arch.py <path to PE file>
```

## Example

```shell
$ python pe_arch.py samples/helloworld-i386.exe
x86 32-bit
$ python pe_arch.py samples/helloworld-amd64.exe
x86_64
$ python pe_arch.py samples/helloworld-arm64.exe
ARM64
```

## Dependencies

- [pefile](https://pypi.org/project/pefile/)

```shell
pip install pefile
```

## Extra Information

If you are using Linux or macOS, there's no need to use third-party tools. Just use the powerful built-in `file` command.

```shell
$ file samples/helloworld-i386.exe
helloworld-i386.exe: PE32 executable (console) Intel 80386, for MS Windows
$ file samples/helloworld-amd64.exe
helloworld-amd64.exe: PE32+ executable (console) x86-64, for MS Windows
$ file samples/helloworld-arm64.exe
helloworld-arm64.exe: PE32+ executable (console) Aarch64, for MS Windows
$ file HELLO.EXE
HELLO.EXE: MS-DOS executable
```
