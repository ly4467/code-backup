i = 1
inv = {}
while i <= 3:
    goods = input("请输入商品编号和商品名称进行商品入库，每次只能输入一件商品：")
    num = int(goods[0:4])
    name = goods[4:]
    if inv.get(num,0) == 0:
        inv.setdefault(int(num),name)
    else:
        print("已在库存中！")
    i += 1


waittobuy = {}
while True:
    num_buy = int(input("请输入要购买的商品编号："))
    a = inv.get(num_buy,0)
    if num_buy == 0:
        break                                       #按0退出购物
    elif a == 0:
        print("该商品不存在！")
    else:
        waittobuy.update({num_buy:a})
        print("商品已添加进购物车！")
    i += 1


print("================分割线==================\n","您购物车已经选择的商品为：")
a = list(waittobuy.items())                         #把购物车换成列表结构并进行反转，使最后加入购物车的商品在最上面
a.reverse()
for i in range(len(a)):
    print(a[i][0],a[i][1])