# Integer Overflow

## integer-overflow-1.0

直接输入一个溢出上限的数即可。

## integer-overflow-1.1

`read_flag`地址为`0x4012AB`

input > 256 时，可以满足整数大小检查条件（低两字节表示的数小于 80 ），同时造成 buffer overflow

通过 buffer overflow 修改返回地址，召唤`read_flag`函数

## integer-over-flow-3.0

该题目要构造一个payload使得能够通过整数溢出的三个条件，注意到要赋值的变量均是有符号整数而在比较中强转成了无符号整数，这道题因为前道题输入即所得的思维定势很容易根据判断条件构造`payload` `ffffffff88889527`

但这道题的关键在于读入函数 `read_hex_long()`

该函数调用`strol()`

`strtol`只能返回带符号的整数，如果pszValue是个无符号数，且值 > 0x7FFFFFFF,返回值为0x7FFFFFF ,即INT_MAX;
int nValue = strtol(pszValue ,NULL,16);

于是输入 `ffffffff888879527` 时都将发生整数溢出，并不能完成判断，(调试即可发现)，理论分析其都超过了最大有符号整数的表示，于是要构造该payload要使用符号扩展，即输入一个负数。我们可以看到payload代表一个负数的补码所以我们只需要求其对应正数原码再在前面填负号即可，f取反后为0，故只要从88889527开始转换即可(取反加1) 最终得到`-77786AD9`

