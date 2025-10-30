RA=[]
print("RAV:")
for i in range(0,9):
    RA.append(int(input(f"RAV {i+1}: ")))
RAA=[0]*9
for i in range(2,7):
    RAA[i]=RA[i]
RAA[0]=RA[1]
RAA[1]=RA[0]
RAA[7]=RA[8]
RAA[8]=RA[7]
print("RA novo:")
for i in range(0,9):
    print(f"RA {i+1}: {RAA[i]}")