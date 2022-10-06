'''
宠物编号
宠物名字
宠物类型
寄养价格

功能：
添加新宠物
显示所有宠物
查询特定宠物
退出程序
'''

# def add_pet():
#     pet_id = input("请输入宠物编号：")
#     pet_name = input("请输入宠物名字：")
#     pet_type = input("请输入宠物类型：")
#     pet_price = input("请输入寄样价格：")
#     with open('pet_info','a') as f:
#         f.write("{} {} {} {}\n".format(pet_id,pet_name,pet_type,pet_price))
#     print('添加成功！')


# def show_pet():
#     with open('pet_info','r') as f:
#         raw_data = f.read()
#     return "宠物ID\t宠物姓名\t宠物类型\t寄样价格\n" + raw_data

# def search_pet():
#     pet_name = input("请输入宠物名字：")
#     with open('pet_info','r') as f:
#         pet_list = f.read().split('\n')
#     for pet in pet_list:
#         if pet_name == pet.split(' ')[1]:
#             return "宠物ID\t宠物姓名\t宠物类型\t寄样价格\n" + pet

# reminder = '''
# 1.添加宠物
# 2.所有宠物
# 3.查询宠物
# 4.退出
# '''
# while 1:
#     print(reminder)
#     choose = input("please choose your function:")
#     if choose == '1':
#         add_pet()
#     elif choose == '2':
#         print(show_pet())
#     elif choose == '3':
#         print(search_pet())
#     elif choose == '4':
#         break
#     else:
#         continue

# print('已退出')


#类方法

class Pet(object):
    def __init__(self,pet_id,pet_name,pet_type,pet_price) -> None:
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_price = pet_price
    
    def pet_to_line(self):
        return "{}&{}&{}&{}\n".format(self.pet_id,self.pet_name,self.pet_type,self.pet_price)

    @classmethod
    def pet_with_line(cls,line):
        pet_id,pet_name,pet_type,pet_price = line.replace('\n','').split('&')
        return Pet(pet_id,pet_name,pet_type,pet_price)

class PetManager(object):
    __instance = None
    __filename = 'pet_book.txt'
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super(PetManager,cls).__new__(cls,*args,**kwargs)
        return cls.__instance
    
    def add_pet(self,pet_id,pet_name,pet_type,pet_price):
        pet = Pet(pet_id,pet_name,pet_type,pet_price)
        with open(PetManager.__filename,'a') as f:
            line = pet.pet_to_line()
            f.write(line)
    
    def list_pet(self):
        pet_list = []
        with open(PetManager.__filename,'r') as f:
            for line in f:
                pet = Pet.pet_with_line(line)
                pet_list.append(pet)
        return pet_list

    def search_pet(self,name):
        pet_list = []
        with open(PetManager.__filename,'r') as f:
            for line in f:
                pet = Pet.pet_with_line(line)
                if pet.pet_name == name:
                    pet_list.append(pet)
        if len(pet_list) > 0:
            return pet_list
        else:
            return None


class Application(object):
    __instance = None
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super(Application,cls).__new__(cls,*args,**kwargs)
        return cls.__instance
    
    def __input_pet_info(self):
        self.pet_id = input("请输入宠物编号：")
        self.pet_name = input("请输入宠物名字：")
        self.pet_type = input("请输入宠物类型：")
        self.pet_price = input("请输入寄样价格：")

    def run(self):
        binner = '''1.添加宠物
2.所有宠物
3.查询宠物
4.退出'''
        while 1:
            print(binner)
            choose = input("please choose your function:")
            if choose == '1':
                self.__input_pet_info()
                PetManager().add_pet(self.pet_id,self.pet_name,self.pet_type,self.pet_price)
                print("宠物添加成功")
            elif choose == '2':
                print(PetManager().list_pet())
            elif choose == '3':
                name = input("请输入宠物名字")
                print(PetManager().search_pet(name))
            elif choose == '4':
                break
            else:
                continue


def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()