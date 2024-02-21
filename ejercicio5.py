import numpy as np

m = np.zeros((10,15))

def shape(m: list[list[int]]) -> tuple[int,int]:
    return len(m),len(m[0])

def zeros_matrix(n: int, m: int) -> list[list[int]]:
    matrix: list[list[int]] = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
    return matrix

def multiplicacion_matriz(m_1: list[list[int]], m_2: list[list[int]]) -> list[list[int]]:
    m_ceros = zeros_matrix(shape(m_1)[0],shape(m_2)[1])
    for i in range(len(m_1)):
        for j in range(len(m_2[0])):
            for k in range(len(m_2)):
                m_ceros[i][j] += m_1[i][k] * m_2[k][j]
    return m_ceros
                                         
def main():
    m_1: list[list[int]] = [[1,5,8],[4,6,7],[2,5,10]]
    m_2: list[list[int]] = [[2,4],[9,0],[0,11]]
    print(multiplicacion_matriz(m_1, m_2))
    print(np.array(m_1).dot(m_2))

if __name__  == "__main__":
    main()