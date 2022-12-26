import numpy as np

# 保存结点信息的模板
class Node:
    def __init__(self, parent_node, left_node, right_node, dim):
        self.parent_node = parent_node
        self.left_node = left_node
        self.right_node = right_node
        self.dim = dim

class KdTree:
    def __init__(self, data):
        self.root_node = self.createtree(data, 0)   # 默认从第一个特征开始排序分割
        self.nearest_dis, self.nearest_node = np.inf, []    # 初始化距离跟最近结点

    # 递归创建kd树
    def createtree(self, data, dim):

        # 判断下面是否还有子结点，没有的话返回空值
        if len(data) == 0:
            return None

        # 将数据按照选定特征排序，花式索引
        data_sorted = data[np.argsort(data[...,dim])]

        # 找出中位数点的索引，如果偶数则选择右边(较大)的点
        middle_index = len(data_sorted)//2

        # 创建左右子节点和父节点，调用Node类来保存父节点坐标，包含的子节点，分类特征所有信息
        left_node = self.createtree(data_sorted[:middle_index], (dim+1)%len(data[0]))
        right_node = self.createtree(data_sorted[middle_index+1:], (dim+1)%len(data[0]))   # 注意取左不取右，这里取左下标要加1
        parent_node = Node(data_sorted[middle_index], left_node, right_node, dim)

        return parent_node

    # 查找kd树上最近的结点
    def nearest(self, target_node):

        # 递归查找函数
        def search(node):
            if node != None:

                # dis:当前结点跟目标点的二范数距离
                dis = np.linalg.norm(target_node - node.parent_node)
                # depth:当前深度的结点对应特征的值跟目标点的特征值的差，即目标点到切割面的直线距离
                depth = target_node[node.dim] - node.parent_node[node.dim]

                # 递归查找目标点所属分支，node为类，node.left_node可以调用左子节点
                search(node.left_node if depth<0 else node.right_node)

                # 判断距离是否小于最短距离，小于则更新最短距离为当前距离，最近点更新为当前结点
                if dis < self.nearest_dis:
                    self.nearest_dis, self.nearest_node = dis, node.parent_node

                # 如果depth小于最短距离，说明另外一个子平面可能有距离更近的结点
                elif np.abs(depth) < self.nearest_dis:
                    # 要去另外一个子平面查找结点，所以depth判断条件和上面相反
                    search(node.left_node if depth>0 else node.right_node)

        node = self.root_node
        search(node)
        return self.nearest_dis, self.nearest_node


data = np.array([[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]])
kdtree = KdTree(data)
nearest_dis, nearest_node = kdtree.nearest(np.array([0.1,-8]))
print("nearest-distance:", nearest_dis)
print("nearest-node:", nearest_node)