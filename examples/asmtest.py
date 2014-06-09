from pwn import *
context(arch='i386', os='linux', net='tcp4')

shellcode = shellcraft.i386_to_amd64()
shellcode_asm = asm(shellcode)

print enhex(shellcode_asm)
print disasm(shellcode_asm)
