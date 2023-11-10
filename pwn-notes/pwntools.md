# pwntools

## pwntools 1.0

- p8, p16, p32 等函数需要与context类型配合使用。
  具体见 [pwnlib.util.packing](https://docs.pwntools.com/en/stable/util/packing.html#)
- 在windows下如果找不到p8等函数，切换到linux环境安装较方便。

## pwntools 1.1

- 同上。

## pwntools 2.0

- [Assembly reference](https://www.felixcloutier.com/x86/)

- ```python
  # contexts
  context.log_level = 'debug'
  context.os = 'linux'
  context.arch = 'amd64'
  ```

- ```python
  # No sendlines, it would append a '\n' after your assembly instructions
  eg. io.sendlineafter -> io.sendafter
  ```

- ```python
  # 避免一次无法接收全部
  while True:
      io.recv()
  ```

## pwntools 2.5

- ```assembly
  # the top value of the stack = abs(the top value of the stack)
  pop rax
  mov rbx, rax
  neg rbx
  cmovl rax, rbx
  push rax
  ```

## pwntools 3.0

- 需要编辑**所有**笔记本再将需要置状态的笔记本置为“废弃”。

  ```python
  # belike:
  content = ["hello ", "world,", " ", "magic ", " ", "notebook"]
  ```

  

- 采用循环解题。
