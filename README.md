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



