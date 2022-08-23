def readMacros(macros):
    f = open("C:\\Users\\lucas\\Documents\\exemplo.txt", "r")
    linhas = f.readlines()
    listaExp = []
    listaArgExp = []
    listaQuantExp = []
    argumentos = 0
    for i in range(len(linhas)):
        if linhas[i][0] == "<":
            vezQueEntrou = 0
            finalNome = 0
            for j in range(len(linhas[i])-1):
                if linhas[i][j] == ">":
                    vezQueEntrou += 1
                    if vezQueEntrou == 1:
                        finalNome = j+1
                        listaExp.append(linhas[i][0:finalNome])
                    if vezQueEntrou == 2:
                        listaArgExp.append(linhas[i][finalNome+5:])
                        argumentos +=1
                        listaQuantExp.append(argumentos)
        if linhas[i][0] == "|":
            listaArgExp.append(linhas[i][2:])
            argumentos +=1
    listaQuantExp.append(argumentos)   
    f.close()
    return(listaExp, listaArgExp, listaQuantExp)

def escolha(nome, listaExp, listaArgExp, listaQuantExp):
    print ("Expressão:")
    print(nome)
    num = 0
    for k in range(len(listaExp)):
        if nome == listaExp[k]:
            num = k
    print(num)
    print ("Qual das opções da expressão você deseja utilizar?:")
    print (listaArgExp[listaQuantExp[num]-1:listaQuantExp[num+1]])
    expressao = int(input())
    print(listaArgExp[listaQuantExp[num]-2+expressao])
    return(listaArgExp[listaQuantExp[num]-2+expressao])

def subst(entrada, saida, listaExp, listaArgExp, listaQuantExp):
    f = open(entrada, "r")
    s = open(saida, "w")
    linhas = f.readlines()
    jaEntrou = 0
    for linha in linhas:
        lista_linha = linha.split()
        if linha[0] == "<":
            jaEntrou = 0
        for palavra in lista_linha:
            for i in range(len(listaExp)):
                if palavra == listaExp[i] and jaEntrou == 0:
                    jaEntrou = 1
                    expressao = escolha(listaExp[i], listaExp, listaArgExp,listaQuantExp)
                    s.write(listaExp[i])
                    s.write(" ::= ")
                    s.write(expressao)
                    s.write('\n')

    s.close()
    f.close()
listaExp, listaArgExp, listaQuantExp = readMacros("macros.txt")
subst("C:\\Users\\lucas\\Documents\\exemplo.txt", "C:\\Users\\lucas\\Documents\\saida.txt", listaExp, listaArgExp, listaQuantExp)



