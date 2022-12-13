
def input_stu_id():
    """输入学生id并判断输入的合法性"""

    while True:
        try:
            stu_id = int(input("请输入学生id:"))
        except:
            print("输入学生id有误，请重新输入")
            continue
        else:
            return stu_id
        break


def read_stu_file():
    """
    打开项目文件夹的students.txt文件读取出内容存在stu_info_cache中并清空内容

    stu_info_cache存储的数据格式为list中每个元素都是dict，如下所示：
    [{dict1},{dict2},....,{dictN}]
    如果文件中没有存储内容则返回[]

    """

    with open("students.txt", "a+") as students:
        students.seek(0)
        stu_info_cache = students.read().split("\n")
        stu_info_cache.pop()  # 删除列表中最后一个空字符串

        # 将存储学生信息列表中的字符串替换成字典
        for num,i in enumerate(stu_info_cache):
            stu_info_cache[num] = dict(eval(i))

        students.seek(0)    # 指针重新指向文件开头
        students.truncate(0)    # 清空文本中的内容，准备之后重新写入数据
        return stu_info_cache


def ask_if_continue(stu_info_cache):
    """询问是否继续本操作，判断输入合法性。如果否则将数据写入文件，返回0。是则只返回1"""

    while True:
        exit = input("是否继续本操作(y/n):")
        if exit in ["y", "Y", "n", "N"]:
            break
        else:
            print("输入有误,请重新输入")

    if exit in ["y","Y"]:
        return 1

    else:
        # 将stu_info_cache中内容写入students.txt中
        write_stu_file(stu_info_cache)
        print("数据已经写入到文件中，将回到主界面")
        return 0


def search_stu_id(stu_info_cache,stu_id):
    """在stu_info_cache查找对应id的学生信息，找到学生信息所在列表的下标，没找到则返回-1"""

    a = 0
    for num,info_dict in enumerate(stu_info_cache):
        if info_dict["student_id"] == stu_id:
            a = 1
            break

    if a == 0:
        return -1
    elif a == 1:
        return num


def input_stu_score():
    """输入学生成绩并判断合法性"""

    while True:
        try:
            stu_en = int(input("请输入学生英语成绩(0~100):"))
            stu_py = int(input("请输入学生python成绩(0~100):"))
            stu_ja = int(input("请输入学生java成绩(0~100):"))
        except:
            print("输入学生成绩有误，必须是整数，请重新输入")
            continue
        else:
            if 0 <= stu_en <= 100 and 0 <= stu_py <= 100 and 0 <= stu_ja <= 100:
                return stu_en,stu_py,stu_ja
                break
            else:
                print("输入学生成绩有误，必须是0~100，请重新输入")


def print_stu_info(stu_info_cache,stu_id):
    """根据学生id打印学生信息一次"""

    for info_dict in stu_info_cache:
        if info_dict["student_id"] == stu_id:

            total_score = info_dict["english_score"] + info_dict["python_score"] + info_dict["java_score"]
            break

    print("{:^16}{:<16}{:<16}{:<16}{:<16}{:<16}".format(info_dict["student_id"], info_dict["student_name"],
                                                        info_dict["english_score"], info_dict["python_score"],
                                                        info_dict["java_score"], total_score))


def write_stu_file(stu_info_cache):
    """将stu_info_cache中内容写入students.txt中"""

    with open("students.txt", "a+") as students:
        # 写入数据并末尾加上换行符，如果没有要写入数据则直接退出
        if stu_info_cache != []:
            for i in stu_info_cache:
                students.write(str(i) + "\n")


def print_stu_score(stu_info_cache,mode_subject,mode_rank):
    """按照输入的排序方式打印排序后学生信息"""

    # 设置sorted是否按照逆序排序
    if mode_rank == 0:
        mode_rank = True
    else:
        mode_rank = False

    # 给列表中每个学生信息的字典中加上总成绩的key,value
    for info_dict in stu_info_cache:
        total_score = info_dict["english_score"] + info_dict["python_score"] + info_dict["java_score"]
        info_dict["total_score"] = total_score

    # 将学生信息按照不同科目进行排序，形成新的列表
    english_sorted = sorted(stu_info_cache,key=lambda x: x["english_score"], reverse=mode_rank)
    python_sorted = sorted(stu_info_cache,key=lambda x: x["python_score"], reverse=mode_rank)
    java_sorted = sorted(stu_info_cache,key=lambda x: x["java_score"], reverse=mode_rank)
    total_sorted = sorted(stu_info_cache,key=lambda x: x["total_score"], reverse=mode_rank)

    # 根据选择的不同科目来设定stu_info_cache对应的排序好的列表
    if mode_subject == 0:
        stu_info_cache = total_sorted
    elif mode_subject == 1:
        stu_info_cache = english_sorted
    elif mode_subject == 2:
        stu_info_cache = python_sorted
    elif mode_subject == 3:
        stu_info_cache = java_sorted

    print("-" * 96)
    print("{:^16}{:<16}{:<16}{:<16}{:<16}{:<16}".format("ID", "Name", "English_score", "Python_score", "Java_score","Total_score"))
    print("-" * 96)

    # 循环打印所有的学生信息
    for info_dict in stu_info_cache:
        total_score = info_dict["english_score"] + info_dict["python_score"] + info_dict["java_score"]
        print("{:^16}{:<16}{:<16}{:<16}{:<16}{:<16}".format(info_dict["student_id"], info_dict["student_name"],
                                                            info_dict["english_score"], info_dict["python_score"],
                                                            info_dict["java_score"], total_score))
    print("-" * 96, "\n"*2)