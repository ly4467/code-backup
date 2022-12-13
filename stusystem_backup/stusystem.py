#!/usr/bin/python3.10
# 引用实现系统功能文件
import sysfunc.func

"""这是学生管理系统主程序"""

# 显示主菜单功能
def menu():
    print("学生管理系统".center(50,"="))
    print("功能菜单".center(50,"-"))
    print("\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t5.排序")
    print("\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t0.退出系统")
    print("-"*52,"\n")

# 主功能函数
def main():
    while True:

        # 显示主菜单
        menu()

        # 判断输入的合法性，并且把模式数字赋给mode变量
        while True:

            try:
                mode = int(input("请输入需要进行的操作的数字:"))
            except:
                print("您输入的数字有误！请重新输入。")
                continue

            # 判断mode是否对应着提供的功能
            if mode in [0,1,2,3,4,5,6,7]:
                break
            else:
                print("您输入的数字有误！请重新输入。")
                continue


        if __name__ == "__main__":

            # 根据mode数字选择不同的模式
            if mode == 0 :

                # 询问用户是否需要退出系统
                exit = input("确认要退出系统吗(y/n):")
                if exit in ["y","Y"]:
                    print("感谢使用学生系统！")
                    break
                elif exit in ["n","N"]:
                    pass
                else :
                    print("输入有误,返回选择菜单并请重新输入")

            elif mode == 1 : sysfunc.func.insert()
            elif mode == 2 : sysfunc.func.search()
            elif mode == 3 : sysfunc.func.delete()
            elif mode == 4 : sysfunc.func.modify()
            elif mode == 5 : sysfunc.func.sort()
            elif mode == 6 : sysfunc.func.total()
            elif mode == 7 : sysfunc.func.show()

main()
