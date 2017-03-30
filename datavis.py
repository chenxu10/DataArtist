# 调用Matplotlib中的pyplot以及plt
# 绘制一个简单的线图
from matplotlib import pyplot as plt

years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

# 创建一幅图，x轴是年份，y轴是gdp
plt.plot(years,gdp,color='green',marker='o',linestyle='solid')

# 添加一个标题
plt.title("NominalGDP")
# 给y轴添加标记
plt.ylabel("1 billion")
# 新窗口绘图
plt.show()

# 条形图：离散项目的数量变化
movies=["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars=[5,11,3,8,10]

# 定义左侧x坐标[xs]
xs=[i+0.1 for i, _ in enumerate(movies)]

# 使用左侧x坐标和高度[num_oscars]
plt.bar(xs,num_oscars)

plt.ylabel("The Amount of Oscar")
plt.title("The movie I like")

# 使用电影的名字标记x轴，位置在x轴上的条形的中心
plt.xticks([i+0.5 for i, _ in enumerate(movies)],movies)
plt.show()

# 条形图：取值是如何分布的
from collections import Counter
def make_chart_histogram(plt):
    grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
    decile = lambda grade: grade // 10 * 10 
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()], # shift each bar to the left by 4
            histogram.values(),                # give each bar its correct height
            8)                                 # give each bar a width of 8
    plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105,
                                               # y-axis from 0 to 5
    plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution of Exam 1 Grades")
    plt.show()
	
make_chart_histogram(plt)

# 统计学上的欺诈：y轴不是从0开始
# 线图：事物的变化趋势
def make_chart_several_line_charts(plt):

    variance     = [1,2,4,8,16,32,64,128,256]
    bias_squared = [256,128,64,32,16,8,4,2,1]
    total_error  = [x + y for x, y in zip(variance, bias_squared)]

    xs = range(len(variance))

    # we can make multiple calls to plt.plot 
    # to show multiple series on the same chart
    plt.plot(xs, variance,     'g-',  label='variance')    # green solid line
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')      # red dot-dashed line
    plt.plot(xs, total_error,  'b:',  label='total error') # blue dotted line

    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means "top center"
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

make_chart_several_line_charts(plt)	

# 散点图：社交网站上
# 朋友个数与在社交网站上花的时间
def make_chart_scatter_plot(plt):

    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)
    
    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                     xy=(friend_count, minute_count), # put the label with its point
                     xytext=(5, -5), # but slightly offset
                     textcoords='offset points')

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()
	
make_chart_scatter_plot(plt)
# plt.axis("equal")更精确
# 统计学会撒谎

# 数据可视化
# seaborn
# D3.js
# Bokeh
# ggplot2
# 《现代统计图形》
