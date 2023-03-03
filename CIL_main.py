"""
sys主程序
"""

from tools import *


def main():
    while True:
        # 1.显示菜单
        show_menu()
        # 2.用户交互
        action = input("choose:")
        '''action==0|==1|==2...'''
        if action in ['1', '2', '3']:
            if action == '1':  # 添加
                new_one()
            elif action == '2':  # 显示
                show_all()
            elif action == '3':  # 搜索
                search()

        elif action == '0':  # 退出
            print("END !")
            exit()
            break

        else:
            print("wrong!")

    # 3.数据存储
    with open('data.txt', 'a') as file:
        for item in infos:
            file.write("%s\n" % str(item)[1:-1])

    # 4.循环退出


if __name__ == '__main__':
    main()
