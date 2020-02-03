dict={"kaushal":"RI","neha":"Thalisthar","avinashi":"VAO"}
count=0
for each in dict.keys():
    if dict[each]=="VAO":
        dict[each]="RI"
        count+=1
print("number of changes:",count)
print("modified contents are:")
print(dict.values())
