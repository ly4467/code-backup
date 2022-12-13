import sysfunc.func2

def insert():
    """录入学生信息"""

    # 读取students.txt内容存到stu_info_cache中并清空内容
    stu_info_cache = sysfunc.func2.read_stu_file()

    # 循环输入学生个人信息，直到输入n退出输入
    while True:

        # 输入学生id
        stu_id = sysfunc.func2.input_stu_id()
        # 查询系统中是否已经存在该学生id的信息
        num = sysfunc.func2.search_stu_id(stu_info_cache,stu_id)

        if num != -1:
            print("此学生id已经录入过信息，请重新输入")
            continue

        # 输入学生姓名
        stu_name = input("请输入学生姓名:")

        # 输入学生成绩并判断合法性
        (stu_en,stu_py,stu_ja) = sysfunc.func2.input_stu_score()

        # 将学生的所有信息以str形式存放在stu_info_cache
        stu_info_cache.append({"student_id": stu_id, "student_name": stu_name, "english_score": stu_en,"python_score": stu_py, "java_score": stu_ja})

        # 询问是否继续添加学生信息
        # 如果不再添加学生信息则将stu_info_cache中数据写入文件并返回主界面
        homepage = sysfunc.func2.ask_if_continue(stu_info_cache)
        if homepage == 0: break


def search():
    """查找学生信息"""

    # 读取students.txt内容存到stu_info_cache中并清空内容
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再修改")
        print("返回主界面")
    else:
        while True:

            # 输入学生id
            stu_id = sysfunc.func2.input_stu_id()

            # 查找对应id的学生信息
            num = sysfunc.func2.search_stu_id(stu_info_cache,stu_id)

            if num != -1:

                print("{:^16}{:<16}{:<16}{:<16}{:<16}{:<16}".format("ID","Name","English_score","Python_score","Java_score","Total_score"))
                # 打印id查询到的学生信息
                sysfunc.func2.print_stu_info(stu_info_cache,stu_id)

            else:
                print("输入的学生id不存在，请重新输入")
                continue

            homepage = sysfunc.func2.ask_if_continue(stu_info_cache)
            # 值为0则返回主界面
            if homepage == 0: break


def delete():
    """删除学生信息"""

    # 读取students.txt内容存到stu_info_cache中并清空内容
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再修改")
        print("返回主界面")
    else:
        while True:

            # 输入学生id
            stu_id = sysfunc.func2.input_stu_id()

            # 删除查询出id对应的学生信息
            num = sysfunc.func2.search_stu_id(stu_info_cache,stu_id)

            if num != -1:
                stu_info_cache.pop(num)
            else:
                print("输入的学生id不存在，请重新输入")
                continue

            homepage = sysfunc.func2.ask_if_continue(stu_info_cache)
            # 值为0则返回主界面
            if homepage == 0: break


def modify():
    """修改学生信息"""

    # 读取students.txt内容存到stu_info_cache中
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再修改")
        print("返回主界面")
    else:
        while True:
            # 输入学生id并判断输入的合法性
            stu_id = sysfunc.func2.input_stu_id()

            # 查询出id对应的学生信息在stu_info_cache中的下标
            num = sysfunc.func2.search_stu_id(stu_info_cache,stu_id)

            if num != -1:

                print("请重新输入该学生相关信息")
                # 输入学生id
                stu_id = sysfunc.func2.input_stu_id()

                # 输入学生姓名
                stu_name = input("请输入学生姓名:")

                # 输入学生成绩并判断合法性
                (stu_en, stu_py, stu_ja) = sysfunc.func2.input_stu_score()

                # 从所有学生信息的list中提取出查询学生信息的dict
                info = stu_info_cache[num]
                # 更新学生信息后的dict
                info_after = {"student_id": stu_id, "student_name": stu_name, "english_score": stu_en, "python_score": stu_py, "java_score": stu_ja}

                # 更新学生信息
                info.update(info_after)
                # 将更新后的dict写入所有学生信息的list中
                stu_info_cache[num] = info

            else:
                print("输入的学生id不存在，请重新输入")
                continue

            homepage = sysfunc.func2.ask_if_continue(stu_info_cache)
            # 值为0则返回主界面
            if homepage == 0: break


def sort():
    """通过English，Python，Java成绩，总成绩进行升序或降序排序"""

    # 读取students.txt内容存到stu_info_cache中
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再查询")
        print("返回主界面")
    else:
        while True:

            # 输入不同的学科排序方式赋值给mode_subject并检查合法性
            while True:
                try:
                    print("0.按照Total成绩排序\n1.按照English成绩排序\n2.按照Python成绩排序\n3.按照Java成绩排序")
                    mode_subject = int(input("请输入要选择的排序方式(0~3):"))
                except:
                    print("输入有误，请重新输入")
                    continue
                else:
                    if mode_subject in [0,1,2,3]:
                        break
                    else:
                        print("输入有误，请重新输入")

            # 输入 升序/降序 排序方式赋值给mode_rank并检查合法性
            while True:
                try:
                    print("0.按照成绩由大到小排序\n1.按照成绩由小到大排序\n")
                    mode_rank = int(input("请输入要选择的排序方式(0/1):"))
                except:
                    print("输入有误，请重新输入")
                    continue
                else:
                    if mode_rank in [0,1]:
                        break
                    else:
                        print("输入有误，请重新输入")

            # 按照输入的排序方式打印排序后学生信息
            sysfunc.func2.print_stu_score(stu_info_cache,mode_subject,mode_rank)

            homepage = sysfunc.func2.ask_if_continue(stu_info_cache)
            # 值为0则返回主界面
            if homepage == 0: break


def total():
    """统计学生总人数"""

    # 读取students.txt内容存到stu_info_cache中
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再查询")
        print("返回主界面")
    else:
        i = len(stu_info_cache)
        print("学生总人数为:%d"%(i))

        # 将stu_info_cache中内容写入students.txt中
        sysfunc.func2.write_stu_file(stu_info_cache)


def show():
    """显示所有学生信息"""

    # 读取students.txt内容存到stu_info_cache中
    stu_info_cache = sysfunc.func2.read_stu_file()

    if stu_info_cache == []:
        print("暂无学生信息，请先录入信息后再查询")
        print("返回主界面")
    else:

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

        # 将stu_info_cache中内容写入students.txt中
        sysfunc.func2.write_stu_file(stu_info_cache)

