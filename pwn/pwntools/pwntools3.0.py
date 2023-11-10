# Codes from PZJ

from pwn import *

context.log_level = 'debug'
context.os = 'linux'
context.arch = 'amd64'


p = process("/challenge/pwntools-tutorials-level3.0")

# enter empty contents
content = ["hello ", "world,", " ", "magic ", " ", "notebook"]

for i in range(6):
    p.sendlineafter("Choice >> ", "1")
    p.sendlineafter("Input your notebook index:", str(i))
    p.sendafter("Input your notebook content:", content[i])

p.sendlineafter("Choice >> ", "2")
p.sendlineafter("Input your notebook index:", "1")

p.sendlineafter("Choice >> ", "2")
p.sendlineafter("Input your notebook index:", "5")

for i in range(6):
    p.sendlineafter("Choice >> ", "4")
    p.sendlineafter("Input your notebook index:", str(i))
p.sendlineafter("Choice >> ", "5")

output = p.recvall()
print(output)