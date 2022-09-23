`helloworld-i386.exe`, `helloworld-amd64.exe` and `helloworld-arm64.exe` are all compiled from the well-known [Hello World](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) by MSVC.


`HELLO.EXE` is a 16-bit MS-DOS executable of Hello World.

```shell
masm hello.asm # output HELLO.OBJ
link hello.obj # output HELLO.EXE
```
