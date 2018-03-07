# 定义一个函数，打印列表中每个魔术师的名字
def show_magicians(magician):
    for magician in magicians:
        msg = "\nThis magician is " + magician.title()
        print(msg)

# 在每个魔术师名字前加The great字样
def make_great(magician):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + 'the Great'
        great_magicians.append(great_magician)


    for great_magician in great_magicians:
        magicians.append(great_magician)

# 创建一个列表，存储魔术师名字
magicians = ['john', 'tom', 'cherry', 'wumin']
show_magicians(magicians)

print("\n")

make_great(magicians)
show_magicians(magicians)
    

    
