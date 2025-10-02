def dliny(mat):
    if any(len(mat[0]) != len(mat[s]) for s in range(len(mat))):
        return False
    return True


def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    if dliny(mat) == False:
        return ValueError
    newmat = [[0 for stro in range(len(mat))] for stol in range(len(mat[0]))]
    for strok in range(len(mat)):
        for stolb in range(len(mat[strok])):
            newmat[stolb][strok] = mat[strok][stolb]
    return newmat



def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if dliny(mat) == False:
        return ValueError
    sums = []
    for i in mat:
        sums.append(sum(i))
    return sums



def col_sums(mat: list[list[float | int]]) -> list[float]:
    if dliny(mat) == False:
        return ValueError
    return row_sums(transpose(mat))

print(col_sums ([[1, 2, 3], [4, 5, 6]]))
print(col_sums ([[-1, 1], [10, -10]]))
print(col_sums ([[0, 0], [0, 0]]))
print(col_sums ([[1, 2], [3]]))
