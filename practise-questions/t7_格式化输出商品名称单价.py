goods = {
    1:["电风扇","美的",500],
    2:["洗衣机","TCL",1000],
    3:["微波炉","老板",400]
}
print("格式化输出".center(40,"-"))
print("编号\t\t\t名称\t\t\t品牌\t\t\t单价")
for i in goods:
    print("{:0>6d}\t\t{}\t\t{}\t\t\t¥{:.2f}".format(i,goods[i][0],goods[i][1],goods[i][2]))
