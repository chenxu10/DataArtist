# Python for Linear Algebra
# 向量数字列表
# 把数字表示成向量的形式
# 三维向量
height_weight_age=[70,170,40]
# 四维向量
grades=[95,80,70,23]
# 两个向量做加法
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

v=[1,2]
w=[2,3]
x=[4,5]
y=[6,7]
B=list(zip(v,w))
print (B)
A=vector_add(v,w)
print (A)
# 思考题：如何写一个向量的减法
def vector_subtract(v,w):
	return [v_i - w_i for v_i, w_i in zip(v,w)]
	
C=vector_subtract(v,w)
print (C)

# 多个向量做加法
from functools import reduce
from functools import partial
# 方法一
def vector_sum(vectors):
	return reduce(vector_add, vectors)
vectors=[[1,2],[2,3],[4,5],[6,7]]

D=vector_sum(vectors)
print (D)
# 方法二
vector_sum=partial(reduce,vector_add)
F=vector_sum(vectors)
print (F)

# 向量乘以标量
def scalar_multiply(c,v):
	return[c*v_i for v_i in v]

v=[2,3]	
I=scalar_multiply(2,v)
print (I)

# 计算长度相同的向量的均值
def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

vector_mean(vectors)

# 向量的点乘
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
	
# 通过点乘自己计算向量的平方和
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)
	
H=sum_of_squares(v)
print (H)

# 计算两个向量的距离
import math

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

G=distance(x,y)
print (G)
# 矩阵
# 矩阵列表的列表
A=[[1,2,3],[4,5,6]]
B=[[1,2],[3,4],[5,6]]
# 通过一个矩阵有几行几列来表达矩阵的形状
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols
C=shape(A)
print (C)

# 把每一行都当成一个长度为k的向量
def get_row(A, i):
    return A[i]

# 把每一列都当成一个长度为n的向量
   
def get_column(A, j):
    return [A_i[j] for A_i in A]

# 创建一个5*5的单位矩阵
def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix 
    whose (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]  

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
print (identity_matrix)

# 矩阵的应用
# 应用1：用矩阵表示多维向量的数据集
# 应用2：矩阵表示一个线性函数，将k维的向量映射到一个n维的向量
# 应用3：用矩阵表示二维关系，社会关系刻画

# 参考资料
# 程序员的数学：线性代数
# 可汗学院：线性代数
