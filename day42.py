dict={"kaushal":"RI","neha":"Thalisthar","avinashi":"VAO"}
count=0
for each in dict.keys():
    if dict[each]=="VAO":
        dict[each]="RI"
        count+=1
print("number of changes:",count)
print("modified contents are:")
print(dict.values())
print("contents in the reverse oreder:")
def reverse(key=len(dict)):
    print(dict[key])
    key-=1
    reverse(key)
    
