# Integer Overflow

## integer-overflow-1.0

直接输入一个溢出上限的数即可。

## integer-overflow-1.1

`read_flag`地址为`0x4012AB`

input > 256 时，可以满足整数大小检查条件（低两字节表示的数小于 80 ），同时造成 buffer overflow

通过 buffer overflow 修改返回地址，召唤`read_flag`函数
