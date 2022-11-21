#working to get the final grid to print without quotes and brackets

data = ['1,2,3','a,b,c']
print(*data, sep = "\n")
for sublist in data:
    print(*sublist.split(","), sep='')
