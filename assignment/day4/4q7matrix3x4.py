# 3x4 matrix as list of lists
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 3x4 matrix as tuple of tuples
matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)
def matrix_add_sub(mat1, mat2):
    add_result = []
    sub_result = []

    for i in range(len(mat1)):
        add_row = []
        sub_row = []
        for j in range(len(mat1[0])):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result
addition, subtraction = matrix_add_sub(matrix_list, matrix_tuple)

print("Addition Result:")
for row in addition:
    print(row)

print("\nSubtraction Result:")
for row in subtraction:
    print(row)
