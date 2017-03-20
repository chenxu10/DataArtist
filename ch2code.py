# Readig this data is straightforward with the built in csv module:
import csv
data_file="E:/DataArtist/topincome.csv"
with open(data_file,'r') as csvfile:
	reader=csv.DictReader(csvfile)
	data=list(reader)
	
A=len(data)
print (A)

print (reader.fieldnames)

B=len(reader.fieldnames)
print (B)

import csv
import numpy as np
import matplotlib.pyplot as plt

# 用Python的生成器一行行地读取数据，而不是一次性把所有的数据存入内存
def dataset(path):
	with open(path,'r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			yield row
			
print (set([row["Country"] for row in dataset(data_file)]))
print (min(set([int(row["Year"]) for row in dataset(data_file)])))
print (max(set([int(row["Year"]) for row in dataset(data_file)])))

# 过滤出美国数据进行单独分析
filter(lambda row: row["Country"]=="United States",dataset(data_file))

import csv
import numpy as np

# 最主要的科学绘图包
import matplotlib.pyplot as plt

# 该函数用于导入Dataset
def dataset(path,filter_field=None,filter_value=None):
	with open(path,'r') as csvfile:
		reader=csv.DictReader(csvfile)
		if filter_field:
			for row in filter(lambda row:
				row[filter_field]==filter_value,reader):
					yield row
		else:
			for row in reader:
				yield row
# 绘制图表				
def main(path):
	data=[(row["Year"], float(row["Average income per tax unit"]))
			for row in dataset(path, "Country", "United States")]

# 每个柱体最大的宽度
	width=0.35
# 每个柱体在x轴上的位置
	ind=np.arange(len(data))
	fig=plt.figure()
	ax=plt.subplot(111)
# 使用切片操作加刻度
	ax.bar(ind,list(d[1] for d in data))
	ax.set_xticks(np.arange(0,len(data),4))
	ax.set_xticklabels(list(d[0] for d in data)[0:4],
	 rotation=45)
	ax.set_ylabel("Income in USD")
	plt.title("United States. Average Income 1913-2008")
	plt.show()
	
# 讲解一下if__name__=="__main__"的作用
# Make a script both importable and executable
# 功能一：外部调用时名字为.py的文件名而不是"__main__"
# 功能二：if__name__=="__main__"加入我们希望调试的代码，这样外部模块调用
# 时不会执行我们的调试代码
if __name__=="__main__":
	main("topincome.csv")	

# 提取出特定国家的数据	
def dataset(path,country="United States"):
	"""
	Extract the data for the country provided. Default is United 
		States.
	"""
	with open(path,'r') as csvfile:

	# csv.DictReader遍历数据并用Python内建的filter函数过滤特定的国家
		reader=csv.DictReader(csvfile)
		for row in filter(lambda row: row["Country"]==country,
		 reader):
		   yield row

# 利用Year列从时间中创建一个时间序列
def timeseries(data,column):
	"""
	Creates a year based time series for the give column.
	"""
	for row in filter(lambda row: row[column], data):
		yield (int(row["Year"]),row[column])
			
			
def linechart(series, **kwargs):
	fig=plt.figure()
	ax=plt.subplot(111)
	
	for line in series:
		line=list(line)
		xvals=[v[0] for v in line]
		yvals=[v[1] for v in line]
		ax.plot(xvals,yvals)
		
	if 'ylabel' in kwargs:
		ax.set_ylabel(kwargs['ylabel'])
	if 'title' in kwargs:
		plt.title(kwargs['title'])
		
	if 'labels' in kwargs:
		ax.legend(kwargs.get('labels'))
		
		return fig
		
def percent_income_share(source):
	""" 
	Create Income Share chart
	"""
	columns=(
	"Top 10% income share",
	"Top 5% income share",
	"Top 1% income share",
	"Top 0.5% income share",
	)
	source=list(dataset(source))
	
	return linechart([timeseries(source,col) for col in columns],
					labels=columns,
					title="United States Percentage Income Share",
					ylabel="Percentage")
					


percent_income_share(data_file)
plt.show()



def normalize(data):
	"""
	Normalizes the data set. Expects a timeseries input
	"""
	data=list(data)
	norm=np.array(list(d[1] for d in data), dtype="f8")
	mean=norm.mean()
	norm /= mean
	return zip((d[0] for d in data), norm)

def mean_normalized_percent_income_share(source):
	columns = (
		"Top 10% income share",
		"Top 5% income share",
		"Top 1% income share",
		"Top 0.5% income share",
		"Top 0.1% income share",
	)
	source=list(dataset(source))
	
	return linechart([normalize(timeseries(source,col)) for 
	  col in columns],
					labels=columns,
					title="Mean Normalized U.S. Percentage Income Share", 
					ylabel="Percentage")

mean_normalized_percent_income_share(data_file)
plt.show()


def delta(first,second):
	"""
	Returns an array of deltas for the two arrays.
	"""
	first=list(first)
	years=yrange(first)
	first=np.array(list(d[1] for d in first), dtype="f8")
	second=np.array(list(d[1] for d in second), dtype="f8")
	
	if first.size != second.size:
		first = np.insert(first,[0,0,0,0], [None,None,None,None])
		
	diff=first - second
	return zip(years,diff)
	
def yrange(data):
	"""
	Get the range of years from the dataset
	"""
	years=set()
	for row in data:
		if row[0] not in years:
			yield row[0]
			years.add(row[0])
		
def capital_gains_lift(source):
	"""
	Computes capital gains lift in top income percentages over 
	  time chart
	"""
	columns = (
		("Top 10% income share-including capital gains","Top 10% income share"),
		("Top 5% income share-including capital gains","Top 5% income share"),
		("Top 1% income share-including capital gains","Top 1% income share"),
		("Top 0.5% income share-including capital gains","Top 0.5% income share"),
		("Top 0.1% income share-including capital gains","Top 0.1% income share"),
		("Top 0.05% income share-including capital gains","Top 0.05% income share"),
		)

	source = list(dataset(source))		
	series=[delta(timeseries(source,a),timeseries(source,b)) for a,b in columns]
	
	return linechart(series,labels=list(col[1] for col in columns), title="U.S. Capital Gains Income Lift",
			ylabel="Percentage Difference")
			
capital_gains_lift(data_file)
plt.show()

def average_incomes(source):
	"""
	Compares percentage average incomes
	"""
	columns=(
		"Top 10% average income",
		"Top 5% average income",
		"Top 1% average income",
		"Top 0.5% average income",
		"Top 0.1% average income",
		"Top 0.05% average income",
	)
	
	source=list(dataset(source))
	
	return linechart([timeseries(source,col) for col in columns], labels=columns,title="U.S. Average Income",
			ylabel="Percentage Difference")

average_incomes(data_file)
plt.show()

def average_top_income_lift(source):
	"""
	Compare top percentage avg income over total avg
	"""
	
	columns=(
	    ("Top 10% average income","Top 0.1% average income"),
		("Top 5% average income","Top 0.1% average income"),
		("Top 1% average income","Top 0.1% average income"),
		("Top 0.5% average income","Top 0.1% average income"),
		("Top 0.1% average income","Top 0.1% average income"),
		("Top 0.1% average income","Top 0.1% average income"),
		)
		
	source=list(dataset(source))
	series=[delta(timeseries(source,a),timeseries(source,b)) for a,b in columns]
		
	return linechart(series,labels=list(col[0] for col in columns),
						title="U.S. Income Disparity",
						ylabel="2008 US Dollars")

average_top_income_lift(data_file)
plt.show()


def stackedarea(series,**kwargs):
	fig=plt.figure()
	axe=fig.add_subplot(111)
	
	fnx=lambda s:np.array(list(v[1] for v in s), dtype="f8")
	yax=np.row_stack(fnx(s) for s in series)
	xax=np.arange(1917,2008)
	
	polys=axe.stackplot(xax,yax)
	axe.margins(0,0)
	
	if 'ylabe' in kwargs:
		axe.set_ylabel(kwargs['ylabel'])
	
	if 'labels' in kwargs:
		legendProxies=[]
		for poly in polys:
			legendProxies.append(plt.Rectangle((0,0),1,1,
			  fc=poly.get_facecolor()[0]))
			  
		axe.legend(legendProxies,kwargs.get('labels'))
	if 'title' in kwargs:
		plt.title(kwargs['title'])
	
	return fig

def income_composition(source):
	"""
	Compares income composition
	"""
	
	columns=(
		"Top 10% income composition-Wages, salaries and pensions",
		"Top 10% income composition-Dividends",
		"Top 10% income composition-Interest Income",
		"Top 10% income composition-Rents",
		"Top 10% income composition-Entrepreneurial income",
		)
	source=list(dataset(source))
	labels=("Salary","Dividends","Interest","Rent","Business")
	return stackedarea([timeseries(source,col) for col in columns],labels=labels,title="U.S. Top 10% Income Composition",ylabel="Percentage")

income_composition(data_file)
plt.show()

	
	


	 
