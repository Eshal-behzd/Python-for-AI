for i in range(3):
    print("Hello World!")

for word in "python":  
    print(word)  

i = 4
rows = i
cols = i
matrix =[]    
for r in range(rows):
    row =[]
    for c in range(cols):
        row.append("0")
    matrix.append(row)
for row in matrix:
    print(" ".join(map(str,row)))        

a = 4
ro = a
co = a
mat = [] 
for b in range(ro):
    c = []
    for d in range(co):
        c.append("*")
    mat.append(c)
for c in mat:
    print(" ".join(map(str,c)))
    
k = 4
for level in range(1, k + 1):
    print(" " * (rows - level ) + "*" * (2 * level - 1))         #"space" (4 - 1) "*" * (2 * 1 - 1 )

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1 
     