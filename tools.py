# @FileName   :tools.py
# @Time       :2023/3/1 1:45
# @Author     :riyo
"""
tools of sys
"""
infos = []
header = ["name", "age"]

def deal_info(find):
    """

    :param find:查到的信息
    :return:
    """
    action=input("choose:1:改; 2:删; 0 :返")
    if action=='1':
        find["name"] = input_info(find["name"],"name:[回车不修改]")
        find["age"] = input_info(find["age"],"age:[回车不修改]")
        print("change successfully")
    elif action=='2':
        infos.remove(find)
        print("remove successfully")

def input_info(value,tip):
    """
    功能集合
    :param value:原有值
    :param tip:输入
    :return:判断修改
    """
    #1.提示输入
    result=input(tip)
    #2.输入不为空,返回输入值
    if len(result)>0:
        return result
    #3.输入为空,保留原有值
    else:
        return value

def show_menu():
    print("sys1.0".center(26, '-'))
    print("*" * 30)
    print("欢迎使用简易信息登记系统\n")
    print("1.新增信息")
    print("2.全部信息")
    print("3.查改信息\n")
    print("0.退出系统")
    print("*" * 30)


def new_one():
    # 1.输入
    print("new:".center(13, '#'))
    name = input("请输入姓名:")
    age = input("请输入年龄:")
    # 2.存储
    info_dict = {"name": name, "age": age}
    # 3.追加列表
    infos.append(info_dict)
    print(infos)
    # 4.成功
    print(f"信息{name}录入成功！")


def show_all():
    print("all:".center(13, '#'))
    # 判断空
    if len(infos) == 0:
        print("None!please new one!")
        return  # 返回调用之所
    # 打印表头
    for title in header:
        print(title, end="\t\t")
    print()
    print("-" * 25)
    # 内容
    for one in infos:
        for val in one.values():
            print(f"{val}", end="\t\t")
        print()


def search():
    print("search:".center(13, '#'))
    name = input("请输入要查询的姓名：")
    for one in infos:
        if one["name"] == name:
            for title in header:
                print(title, end="\t\t")
            print()
            print("-" * 25)
            for val in one.values():
                print(f"{val}", end="\t\t")
            print()
            # 提示操作选择:删除,修改,返回
            deal_info(one)
            break
    else:
        print(f"sorry,no{name}")


if __name__ == '__main__':
    show_all()
