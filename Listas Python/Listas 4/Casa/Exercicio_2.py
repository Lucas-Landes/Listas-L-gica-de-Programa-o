RA=[]
print("RAV:")
for i in range(0,9):
    RA.append(int(input(f"RAV {i+1}: ")))
RAA=[0]*9
for i in range(0,5):
    RAA[i]=RA[i]
RAA[5]=RA[8]
RAA[6]=RA[7]
RAA[7]=RA[6]
RAA[8]=RA[5]
print("RA novo:")
for i in range(0,9):
    print(f"RA {i+1}: {RAA[i]}")