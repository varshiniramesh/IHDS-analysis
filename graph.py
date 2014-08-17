import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from_csv = pd.read_csv('Data.csv')
res=pd.DataFrame(from_csv)
list1=[0]
list2=[0]

#need to make range dynamic
for i in range(1,34):
	x=(np.where(res.stateid==i)[0]).size
	list1.append(x)	
	list2.append(i)
	
n_groups=34
fig, ax =plt.subplots()
index=np.arange(n_groups)
bar_width=1
opacity=0.7

error_config= {'ecolor' : '0.3'}
plt.bar(list2,list1,bar_width,
	alpha=opacity,
	color='g',
	error_kw=error_config,
	label='')

for i,j in zip(list2,list1):
	plt.annotate(str(j),xy=(i,j+1))
#plt.plot(list2,list1,marker="o",color="green")
plt.xlim(1,34)
plt.xlabel("state ID")
plt.ylabel("number of districts")
plt.title("District frequency over states")
#plt.xticks(index,list1)
plt.legend()
plt.tight_layout()
plt.show()

