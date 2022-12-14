# -*- coding: utf-8 -*-


# GLOBALS DICT

from base64 import b16encode, b32encode, b64encode, b16decode, b32decode, b64decode
from builtins import *

globals_names = {k:v for k,v in globals().items()}


# REQUIREMENTS

from pyfade import Colors, Fade
from pycenter import center
from requests import get, post

from random import randint, choice
from os.path import isfile
from os import name, system


def clear():
    system("cls" if name == 'nt' else "clear")

clear()


strings = "abcdefghijklmnopqrstuvwxyz0123456789"


if name == 'nt':
    system("title Đậu Đậu")
    system("mode 160, 40")

encoding = 'utf-8'
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ignore = ("b16encode", "b32encode", "b64encode")


class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "gray" : "\033[38;2;150;150;150m", 
              "darkgray" : "\033[38;2;100;100;100m", 
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    gray = colors['gray']

    darkgray = colors['darkgray']

    white = colors['white']

        
    def printf(text):
        print(Col.darkgray + text)




class Create():
        def __init__(self):
            self.content= ""
        def write(self, content):
            self.content += content






jawbreaker = """
  /$$$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$
| $$_____/| $$$ | $$ /$$__  $$ /$$__  $$| $$__  $$| $$_____/
| $$      | $$$$| $$| $$  \__/| $$  \ $$| $$  \ $$| $$      
| $$$$$   | $$ $$ $$| $$      | $$  | $$| $$  | $$| $$$$$   
| $$__/   | $$  $$$$| $$      | $$  | $$| $$  | $$| $$__/   
| $$      | $$\  $$$| $$    $$| $$  | $$| $$  | $$| $$      
| $$$$$$$$| $$ \  $$|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$$
|________/|__/  \__/ \______/  \______/ |_______/ |________/                                                                      
"""

author = "  # # # {} # # #".format("  Đậu Đậu  ")

print(Fade.Vertical(Colors.white_to_black, center(jawbreaker)))
print(Fade.Horizontal(Colors.black_to_white, center(author)))

print("\n")

service = "https://hastebin.com"

file = input(Col.gray+"  [*] Nhập tên tệp: "+Col.white)

if not isfile(file):
    print()
    input(Col.red+"  [!] Tệp này không tồn tại!"+Col.white)
    exit()

output = input(Col.gray+"  [*] Nhập tên của tệp đầu ra: "+Col.white)
if not output:
    if not isfile("new.py"):
        output = "new.py"
    else:
        x = 1
        while True:
            output = "new" + str(x) + ".py"
            if not isfile(output):
                break
            x += 1



print()
Col.printf("\n  Đang xây dựng tệp bị xáo trộn ... \n")

defined = []

def nfile(file:object, only:bool=False) -> tuple:
    
    temp_names = ["exec", "b16decode", "b32decode", "b64decode"] if only else [name for name in globals_names]

    Col.printf("  Định nghĩa các biến toàn cầu ...")

    for name in temp_names:
        random_name = random()
        if name == "exec":
            exc = random_name
        elif name == "b16decode":
            b16 = random_name
            file.write(f"from base64 import b16decode as {b16};")
            continue
        elif name == "b32decode":
            b32 = random_name
            file.write(f'from base64 import b32decode as {b32};')
            continue
        elif name == "b64decode":
            b64 = random_name
            file.write(f'from base64 import b64decode as {b64};')
            continue
        elif name in ignore:
            continue
        file.write(f"{random_name}={name};")
    return exc, b16, b32, b64

def random(l:int=2) -> str:
    while True:
        rdm = "".join(choice(chars) + choice([choice(chars), str(randint(0,9))]) for _ in range(1, l+1))
        if rdm not in defined:
            defined.append(rdm)
            return rdm


def build():

    with open(file, 'r', encoding=encoding) as f:
        content = f.read()

    Col.printf("  Tạo hastebin ...")

    try:
        response = post(service + "/documents", data=content.encode('utf-8'))

        if response.status_code != 200:
            input(Col.red+f"Error! Hastebin service is maybe down. Response status code: {response.status_code}"+Col.white)
            exit()
    except:
        input(Col.red+"Error! Hastebin service is maybe down."+Col.white)
        exit()
        
    url = service + "/raw/" + response.json()['key']
    Col.printf(f"  Đã tạo Hastebin! Url: {url}.")


    file_1 = Create()

    exc, b16, b32, b64 = nfile(file_1)

    urlp = random()
    req = random()

    Col.printf("  Đang nhập các yêu cầu HTTP lib ...")
    file_1.write(f"from urllib.request import urlopen as {urlp}, Request as {req};")

    chars_list = random()
    Col.printf("  Tạo danh sách nội dung ...")
    file_1.write(f"{chars_list}=[];")
    content = f"""{exc}({urlp}({req}("{url}",headers=%s)).read())""" % "{'user-agent':''}"


    Col.printf("  Mã hóa nội dung ...")

    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)


    random_chars_list = []

    Col.printf("  Xây dựng danh sách nội dung ...")

    for char in content:
        random_char = random()
        random_chars_list.append(random_char)
        file_1.write(f"{random_char}='{char}';")

    random_append_function = random()
    file_1.write(f"{random_append_function}={chars_list}.append;")

    for random_char in random_chars_list:
        file_1.write(f"{random_append_function}({random_char});")

    content_name = random()
    Col.printf("  Đang tạo biến cần giải mã ...")
    file_1.write(f"{content_name} = ''.join({chars_list});")

    Col.printf("  Xây dựng obfuscator ...")

    dcontent = f"{exc}({b64}({b32}({b16}({content_name}))));"

    file_1.write(dcontent)



    content = file_1.content
    
    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)


    file_2 = Create()


    exc, b16, b32, b64 = nfile(file_2)


    Col.printf("  Đang xây dựng obfuscator thứ hai ...")



    file_2.write(f'{exc}({b64}({b32}({b16}("{content}"))));')

    Col.printf("\n  Tạo nội dung cuối cùng ...")
    content = file_2.content

    Col.printf("  Viết nội dung ...")

    with open(output, 'w', encoding=encoding) as f:
        f.write(content)



try:
    build()
    print("\n")
    input(Col.gray+"  Xong!"+Col.white)
except Exception as e:
    input(Col.red+"  Lỗi! [{}]".format(e)+Col.white)