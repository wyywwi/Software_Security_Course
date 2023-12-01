# Buffer Overflow

## buffer-overflow-1.0

下载可执行文件，采用IDA调试，可见`char buffer[0x10];`一句对应变量为`var_20 = byte ptr -20h`，也就是说它在栈当中的位置为`-0x20`；对应地，`long magic`所在位置为`-0x8`，二者间隔为`0x18`，大于`0x10`,**buffer和magic在栈中存在间隔，需要填充**。

```python
# 先填充前0x18个字符
b'123456789012345678901234'
# 再输出payload
p64(0xdeadbeef)
```

## buffer-overflow-1.1

间隔和上一题相同，修改的变量为函数指针。采用IDA查看`read_flag`函数地址得到`0x4012D7`，则将payload末尾改为`0x4012D7`即可。
