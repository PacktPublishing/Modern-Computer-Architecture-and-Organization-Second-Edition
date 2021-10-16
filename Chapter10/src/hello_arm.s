.text
.global _start

_start:
    mov     r0, #1       // int fd 1 (stdout)
    ldr     r1, =message // const void *buf
    mov     r2, #count   // size_t count
    mov     r7, #4       // syscall 4 (sys_write)
    svc     0

    mov     r0, #0       // int status (0=OK)
    mov     r7, #1       // syscall 1 (sys_exit)
    svc     0
        
.data
message:
    .ascii      "Hello, Computer Architect!"
count = . - message
