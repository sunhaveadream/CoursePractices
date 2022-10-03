#chapter2
#2022/10/3
#author:linxu
#书本代码2.1
print("Hello Python world")
#书本代码2.2
message="Hello Python world"
print(message)
#书本代码2.3
#书本代码2.3.1
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#书本代码2.3.2
#在字符串中使用变量，f是format(设置格式)的简写
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
#使用f字符串可以完成很多任务
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}!")
#使用f字符串来创建消息，再把消息赋给一个变量
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
message=f"Hello,{first_name.title()}!"
print(message)
#f字符串是Python 3.6引入的，使用的是Python3.5或更早的版本，需要使用format()方法
full_name="{}{}".format(first_name,last_name)
#书上代码2.3.3
print("\tpython")
#书上代码2.3.4
favorite_language='python '
favorite_language.rstrip()
#课后练习2.2
#练习2-1 简单消息 将一条消息赋给变量，并将其打印出来
message="python exercises"
print(message)

#练习2-2 多条简单消息 将一条消息赋给变量，变更将其打印出来
message="python exercises"
print(message)
message="python exercises_new"
print(message)

