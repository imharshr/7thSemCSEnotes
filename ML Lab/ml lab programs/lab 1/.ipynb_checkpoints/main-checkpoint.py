import csv

data=[]
with open('Train.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
        print(row)
        
num_attributes=len(data[0])-1

print("The most general hypothesis:",["?"]*num_attributes)
print("The most specific hypothesis:",["\u03B8"]*num_attributes)

S=data[0][:-1]

print("\n Find S: Finding data maximally specific hypothesis")
for i in range (len(data)):
    if data[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if data[i][j]!=S[j]:
                S[j]='?'
    print("The taining example no:",i+1," the hyposthesis is:",S)
print("\n The maximally specific hypohthesis for training set is")
print(S)