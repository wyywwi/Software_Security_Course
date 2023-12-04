#!/opt/pwn.college/python

'''
魔改过的utility.py
添加自动化碰撞md5函数, 调用原版计算方法
代码来源: pwn.hust.college
使用方法: 选择选项4, 等待查看输出
'''

import hashlib
import binascii

file_path = "./elf-crackme-level2.2"
def read_flag():
    # with open('/flag', 'r') as file:
    #     file_contents = file.read()
    #     print(file_contents)
    pass

def calculate_md5(data):
    md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

def md5_check(hex_string):
    hex_string = hex_string.replace(" ", "")  
    binary_data = binascii.unhexlify(hex_string)
    md5_result = calculate_md5(binary_data)
    return md5_result
    print("MD5 Hash:", md5_result)

def patch():
    
    try:
        with open(file_path, "r+b") as file:
            position = int(input("[+] Please enter the position to modify (in hexadecimal, e.g., 0x1000): "), 16)
            new_data = int(input("[+] Please enter the new byte data (in hexadecimal, e.g., 01): "), 16)
            
            file.seek(position)
            file.write(bytes([new_data]))
            
        print("[+] Modification completed!")
    except FileNotFoundError:
        print("[-] Unable to open the file")
    except Exception as e:
        print("[-] An error occurred:", e)

def check():
    try:
         with open(file_path, "rb") as file:
            position = 0x1060
            length = 405
            file.seek(position)
            data_read = file.read(length)
            md5_2 = calculate_md5(data_read)
            print("The current hash is", md5_2)
            if md5_2 == "ba4f77d33e8961855bda04916d50f802":
                print("[+] Modification completed!")
                read_flag();
            else:
                print("[-] Hash verification for the .text segment failed. Please modify it again.")

 
    except Exception as e:
        print("[-] An error occurred:", e)

def auto_modify():
    with open(file_path, "r+b") as file:
        pos_1 = 0x1169
        pos_2 = 0x116A
        position = 0x1060
        length = 405
        flag = 0
        for i in range(0, 256):
            file.seek(pos_1)
            file.write(bytes([i]))
            for j in range(0, 256):
                file.seek(pos_2)
                file.write(bytes([j]))
                file.seek(position)
                data_read = file.read(length)
                md5_2 = calculate_md5(data_read)
                print("i: ", hex(i), "\tj: ", hex(j), "\tThe current hash is", md5_2)
                if md5_2 == "ba4f77d33e8961855bda04916d50f802":
                    print("[+] Modification completed!")
                    print("0x1169: ", hex(i))
                    print("0x116A: ", hex(j))
                    flag = 1
                    break
            if flag == 1:
                break

if __name__ == "__main__":
    print("###")
    print("### Welcome to ./elf-crackme-level2.2!")
    print("###")
    print("")    
    print("Original .text hash is ba4f77d33e8961855bda04916d50f802")
    print("We changed two bytes in the .text segment to 0x9090. Please try to find")
    print("and crack the original result. After completing the repair, execute the check function to get the flag.")
    while True:
        print("Select the action you want to perform:")
        print("1. Modify the ELF file")
        print("2. Check the repaired content")
        print("3. Exit")
        print("4. Auto modify")
        
        choice = input("Enter the option number: ")
        
        if choice == "1":
            patch()
        elif choice == "2":
            check()
        elif choice == "3":
            print("The program has exited.")
            break
        elif choice == "4":
            auto_modify()
        else:
            print("Invalid option, please enter again.")


