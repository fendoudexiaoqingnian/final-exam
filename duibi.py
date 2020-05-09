import os
import numpy as np

MLP_result=[]
ResNet_result=[]
FCN_result=[]
result=[]
wins=[]

MLP_result_path = r'C:\Users\zwy\Desktop\模型加shuffle\MLP_result.txt'
ResNet_result_path = r'C:\Users\zwy\Desktop\模型加shuffle\ResNet_result.txt'
# path = 'C:\Users\zwy\Desktop\模型加shuffle\MLP_result.txt'
MLP_result_file = open(MLP_result_path)
ResNet_result_file = open(ResNet_result_path)
try:
    for line in MLP_result_file:
        line=line.replace("\\n", ",")
        line=line.split(",")
        for num in line:
            MLP_result.append(int(num))
finally:
    MLP_result_file.close()
try:
    for line in ResNet_result_file:
        line=line.replace("\\n", ",")
        line=line.split(",")
        for num in line:
            ResNet_result.append(int(num))
finally:
    ResNet_result_file.close()

MLP_result = np.array(MLP_result)
ResNet_result=np.array(ResNet_result)
print(MLP_result)
print(ResNet_result)

for i in range(0,300):
    if MLP_result[i]==ResNet_result[i]:
        if MLP_result[i]==FCN_result[i]:
            result[i]=MLP_result[i]
            wins[i]=3
        else:
            result[i]=MLP_result[i]
            wins[i]=2
    else:
        if MLP_result[i]==FCN_result[i]:
            result[i] = MLP_result[i]
            wins[i] = 2
        else:
            if ResNet_result[i]==FCN_result[i]:
                result[i] = ResNet_result[i]
                wins[i] = 2
            else:
                result[i]=
                wins[i]=1
print(result)
print(wins)
result_path = 'C:\\Users\\zwy\\Desktop\\result.txt'
result_txt=open(result_path,'w')
for pre in result:
    result_txt.write(str(pre))
    result_txt.write('\n')
result_txt.close()




