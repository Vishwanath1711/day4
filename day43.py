list=["sdmit","ait","nit","kle"]
def interchange(key=0):
    if list[key][0] in "aeiou":
        list[key+1]=list[key]
        key+=1
        interchange(key)
for each in range(0,len(list)):
    print(list[each])
