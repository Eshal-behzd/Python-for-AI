for i in range(3):
    print("outer loop")
    for j in range(1):
        print("    inner loop")

i = 4
rows = i
cols = i
matrix =[]
for r in range(rows):
    row = []
    for c in range(cols):
        row.append("*")
    matrix.append(row)
for row in matrix:
    print(" ".join(map(str,row)))        