import numpy as np

# 将文件中数据以数组形式导入python
# 数组data第一列为所有点的x坐标，第二列为所有点的y坐标
data = np.loadtxt("./ex1data1.txt",delimiter=",")

# 给每个点都插入x0 = 1特征值，广播后插入
data = np.insert(data, 0, np.array([1]), axis=1)

# 将点的坐标信息存储在x,y中，注意y是1维数组
x = data[:, :2]
y = data[:, 2]
# 初始化theta，一定记得设置为浮点类型，否则无法收敛
theta = np.array([0]*(data.shape[1]-1), dtype="f8")

# 计算损失函数的值
def costfunc(x, y, theta):
    # cost function
    cost = (1/(2*len(y)))*np.sum(((np.dot(x,theta) - y))**2)
    return cost

# 进行梯度下降
def gradientdescent(x, y, theta, alpha):

    # 一定记得设置为浮点类型，否则无法收敛
    theta_new = np.array([0]*x.shape[1],dtype="f8")
    loss = np.dot(x,theta) - y

    # gradient descent, 同时赋值theta(j)
    for j in range(x.shape[1]):
        theta_new[j] = theta[j]-(alpha/len(y))*np.sum(loss*x[:, j])
    return theta_new

alpha = 0.01
times = 1000
for _ in range(times):
    cost = costfunc(x, y, theta)
    theta = gradientdescent(x, y, theta, alpha)

print(theta, cost)