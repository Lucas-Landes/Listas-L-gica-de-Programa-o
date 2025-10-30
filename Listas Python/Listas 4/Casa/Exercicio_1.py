RAV=[]
print("RAV:")
for i in range(0,9):
    RAV.append(int(input(f"RAV {i+1}: ")))

RAC=[0]*9
RAC[0]=RAV[0]
RAC[1]=RAV[1]
RAC[2]=RAV[7]
RAC[3]=RAV[6]
RAC[4]=RAV[4]
RAC[5]=RAV[5]
RAC[6]=RAV[2]
RAC[7]=RAV[3]
RAC[8]=RAV[8]
print("RAC:")
for i in range(0,9):
    print(f"RAC[{i+1}]: {RAC[i]}")