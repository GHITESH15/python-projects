kid=[12,56,77,48,89,45,57,14]
evenlist=[]
oddlist=[]
for i in kid:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("even number",evenlist)
print("odd number",oddlist)
