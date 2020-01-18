import xlrd
import math

global n_rows, n_cols, table, Ne, Se, m_m


def read_excel():

	#获取分析数据的excel文件 “32new.xlsx”
	work_data=xlrd.open_workbook(r'33new.xlsx')

	table=work_data.sheets()[0]

	# 行数
	n_rows = table.nrows

	# 列数
	n_cols = table.ncols

	# Ne固定数值 10^7
	Ne=math.pow(10,7)

	# Se固定数值
	Se=40

	# M固定数值
	m_m=3

	print("col: %s"%n_cols + " row: %s"%n_rows)

	#获取第一列的所有值
	y_values=table.col_values(0)

	#获取x轴的值, 数据横坐标值可以更改
	x_values=table.row_values(n_rows-1)
	
	
	# 所有SR的值, SR的值也是变量i 
	sr_list=[]
	for i in range(n_rows-1):
		#65属于可更改数据
		for j in range(1,n_rows):
			sr_01=table.row_values(i)[0]-x_values[j]
			
			sr_list.append(abs(sr_01))

	print("SR:%s"%sr_list+"====lenth:%s"% len(sr_list)+"\n")

	# # 求Ni的值, 并且将值存入数组 
	Ni_list=[]
	Ni=0
	for j in sr_list:
		if j==0:
			Ni=0
		elif j>=40 and j<=400:
			Ni=Ne/math.pow((j/Se),1/m_m)
		else:
			pass
		Ni_list.append(Ni)

	print("Ni:%s"%Ni_list+"====lenth:%s"%len(Ni_list)+"\n")


	# # 从表格里获取ai的值,并且求得Ri的值, ai的值是变量i
	Ri_list=[]
	Ai_list=[]
	for t in range(1,n_cols):
		ai_value=table.col_values(t)
		del(ai_value[-1])
		# print("ai_value:%s"%ai_value+"====lenth====%s"%len(ai_value))
		Ai_list+=ai_value
		# Ai_list.append(ai_value)	

	print("Ai_list:%s"%Ai_list+"====lenth:%s"%len(Ai_list))

	for k in range(len(Ai_list)):
		# print(16)
		if Ni_list[k]>0 or Ni_list[k]<0:
			Ri=Ai_list[k]/Ni_list[k]
			Ri_list.append(Ri)

	print("\n"+"Ri_list:%s"%Ri_list+"====lenth:%s"%len(Ri_list))

	# #获取Nt的值
	Nt=1/(sum(Ri_list))
	
	#打印结果
	print("\n"+"NT value: %s "%Nt)
	

if __name__ == '__main__':
	read_excel()


