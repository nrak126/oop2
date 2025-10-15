import csv

# 頭の体操
# header = [i+1 for i in range(9)]
# matrix_99 = [[j*i for j in header ] for i in header]
header=list(map(lambda x: x+1,range(9))) # [1,2,3,4,5,6,7,8,9]
matrix_99=[]
for i in header:
    col = []
    for j in header:
        col.append(i*j)
    matrix_99.append(col)


# check martrix_99
# print(martrix_99)

# 頭の体操
# odd_index = list(range(9)[::2])) # [0, 2, 4 ,6, 8]
# odd_index = [x for x in range(9)[::2]]
# matrix_99_odd = matrix_99[::2] # 奇数行目(1,3,5,7,9の段)だけ取ってくる
odd_index = list(filter(lambda col_index: (col_index+1)%2==1, range(9))) # [0, 2, 4, 6, 8]
matrix_99_odd = list(map(lambda index: matrix_99[index], odd_index))

# csvファイルへ書き込み
with open('matrix_99_odd.csv', 'w') as f:
    writer = csv.writer(f)
    # writer.writerows(matrix_99_odd) or the below
    for row in matrix_99_odd:
        writer.writerow(row)
