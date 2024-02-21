class Matrix:
    def __init__(seft, m: list[list[int]]):
        seft.m = m
    
    def sum(seft) -> int:
        count = 0
        for i in range(len(seft.m)):
            for j in range(len(seft.m[0])):
                count += seft.m[i][j]
        return count
    
    def columns(seft) -> int:
        return len(seft.m[0])

my_matrix = Matrix([[1,5,8],[4,6,7],[2,5,10]])
my_matrix.sum()

print(my_matrix.sum())
print(my_matrix.m)
print(my_matrix.columns())