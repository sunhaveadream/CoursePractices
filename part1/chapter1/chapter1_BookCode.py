#chapter1_BookCode
#2022/10/6
#author:linxu
"""
这里是《Python编程从入门到实践（第2版）》书上第2章的代码
"""

"""
2.2.1 使用小写的Python变量名 hello_world.py
"""
# message = 'Hello Python world!'
# print(message)

"""
2.3 用引号括起的都是字符串，引号可以是单引号，也可以是双引号
2.3.1 修改字符串大小写的方法#方法是Python可对数据执行的操作 name.py

title() 将每个单词的首字母都改为大写 
upper() 将字符串改为全部大写 
lower() 将字符串改为全部小写
"""
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())

"""
2.3.2 在字符串中使用变量，使用f字符串，f是format（设置格式）的简写 full_name.py
"""
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name}{last_name}"
# message = f"Hello,{full_name.title()}！"
# print(message)

"""
2.3.3 使用制表符或换行符来添加空白#空白泛指如空格、制表符和换行符等任何非打印字符
\t 在字符串中添加制表符 
\n 在字符串中添加换行符
\n\t 让字符串换一行，并在下一行开头添加一个制表符
"""
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

"""
2.3.4 删除额外的令人迷惑的空白

rstrip() 删除字符串末尾的空白
lstrip() 删除字符串开头的空白
strip() 删除字符串两边的空白
"""
# favorite_language=' python '
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())
