list1= list(input("Eneter the number").split(","))
d={}
san_values=[]
for l in list1:
    l1= l.split("=")
    if "s" in l1[0]:
        san_values.append(l[1])
    else:
        d[l1[0]] = l1[1]

d['san_value'] = san_values
print(d)
print(san_values)