# note_function
函数学习笔记
1.让实参变得可选
  在函数中加入if语句，从而让实参变得可选。
  def get_formatted_name(first_name,  last_name, middle_name=' '):
    """返回整齐的姓名"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name   
    return full_name.title()


musician = get_formatted_name('john', 'hooker')

print(musician)
语句中采用if语句判断是否有中间名并输出全名


2.返回字典
  函数可返回任何类型的值。
  
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的相关信息"""
    person = {'first': 'first_name', 'last': 'last_name'}
    return person

musician = build_person('jim', 'hendrix')
print(musician)
将个人名字存储在一个字典中，调用更方便。


3.结合使用函数和循环
greeter.py
def get_formatted_name(first_name,  last_name, middle_name=' '):
    """返回整齐的姓名"""
    full_name = first_name + " " + last_name   
    return full_name.title()


# 这是一个无限循环
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First_name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)
    
    
    加入if语句判断终止条件
    
    
    def get_formatted_name(first_name,  last_name, middle_name=' '):
    """返回整齐的姓名"""
    full_name = first_name + " " + last_name   
    return full_name.title()


# 这是一个无限循环
while True:
    print("\nPlease tell me your name: ")
    print("\nPlease enter 'q' to quit.")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last time: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + " .")

 
3. 传递列表

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + " !"
        print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)
# 将greet_users() 定义为接受一个名字列表，并储存在形参names中.

4. 在函数中修改列表

printing_models.py

# 创建一个列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + " !"
        print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)


5.在函数中修改列表

printing——models.py
# 创建一个列表，包含一些要打印的设计
unprinted_designs = ['iphone case', 'reboot pendant', 'dodecahedron']
completed_models = []


# 模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)


# 显示打印好的所有模型
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

5 传递任意数量的实参
pizza.py

def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print(topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra chese')

*topping 创建一个空元组

def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in topping:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra chese')
通过将print替换为一个循环语句，遍历整个列表

5.1 结合使用位置实参和任意数量实参
def make_pizza(size, *topping):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in topping:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra chese')

5.2 使用任意数量的关键字实参

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
