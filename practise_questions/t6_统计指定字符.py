count_obj = "HelloPython,HelloJava,hellophp"
a = input("请输入要查询字符个数：")    #不区分大小写
i_1 = count_obj.count(a)
i_2 = count_obj.count(a.upper())

# print("{}在{}中一共出现了{}次".format(a,count_obj,i_1 + i_2))  这样写也可以
print(f"{a}在{count_obj}中一共出现了{i_1 + i_2}次")