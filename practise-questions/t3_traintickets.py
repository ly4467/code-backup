train_schedule = {
    "G1569":["北京南-天津南","18:05","18:39","00:34"],
    "G1567":["北京南-天津南","18:15","18:49","00:34"],
    "G8917":["北京南-天津西","18:20","19:19","00:59"],
    "G203":["北京南-天津南","18:35","19:09","00:34"],
}

#展示车次信息给购票者
print("编号\t\t始发站-终点站\t\t出发时间\t到达时间\t历时时长")
print("------------------------------------------------")
for i in train_schedule.items():
    print("{}\t{}\t\t{}\t{}\t{}".format(i[0],i[1][0],i[1][1],i[1][2],i[1][3]))

while True:
    train_num = input("\n请输入要购买的车次：")
    info = train_schedule.get(train_num)
    if info == None:
        print("您输入车次编号有误，请重新输入")
    else:
        break

passenger = input("请输入乘车人姓名，如果是多人请使用逗号分隔：")
print("您已购买了{}次列车，{} {}开，请{}尽快换取纸质车票。【铁路客服】".format(train_num,info[0],info[1],passenger))

