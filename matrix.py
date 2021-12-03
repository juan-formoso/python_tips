# Soma de duas matrizes

def somar(matrizA, matrizB):
		matrizC = []
		for i in range(len(matrizA)):
				linha = []
				for j in range(len(matrizA[i])):
						linha.append(matrizA[i][j] + matrizB[i][j])
				matrizC.append(linha)
		return matrizC

# Subtração de duas matrizes
def subtrair(matrizA, matrizB):
		matrizC = []
		for i in range(len(matrizA)):
				linha = []
				for j in range(len(matrizA[i])):
						linha.append(matrizA[i][j] - matrizB[i][j])
				matrizC.append(linha)
		return matrizC

# Multiplicação de duas matrizes
def multiplicar(matrizA, matrizB):
		matrizC = []
		for i in range(len(matrizA)):
				linha = []
				for j in range(len(matrizB[0])):
						soma = 0
						for k in range(len(matrizA[0])):
								soma += matrizA[i][k] * matrizB[k][j]
				linha.append(soma)
				matrizC.append(linha)
		return matrizC

# Divisão de duas matrizes
def dividir(matrizA, matrizB):
		matrizC = []
		for i in range(len(matrizA)):
				linha = []
				for j in range(len(matrizA[i])):
						linha.append(matrizA[i][j] / matrizB[i][j])
				matrizC.append(linha)
		return matrizC