; Adapted from https://wyding.blogspot.com/2009/04/helloworld-for-16bit-dos-assembly.html

.model small
.stack
.data
    message   db "Hello, World!", "$"
.code
    main    proc
        mov   ax,seg message
        mov   ds,ax
        mov   ah,09
        lea   dx,message
        int   21h
        
        mov   ax,4c00h
        int   21h
    main    endp
end main
