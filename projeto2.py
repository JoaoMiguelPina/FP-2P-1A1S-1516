# 83539 Pedro Caldeira, 85080 Joao Pina   Grupo 56 
#representacao interna escolhida: listas


#-------------------------------------------------------------------------------------------------------------
#----------------------------Funcoes auxiliares---------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#funcao que calcula o maior tuplo dentro de um tuplo

def maior_tuplo(tuplo):         
    maiortuplo= ()
    tuplo = ordena_tuplo(tuplo)     #de forma a facilitar calculos, ordenamos o tuplo principal                           
    for i in range(len(tuplo)-1):   #e vamos buscar o tuplo com maior len 
        if len(tuplo[i+1])>len(tuplo[i]):
            maiortuplo = tuplo[i+1]
    return maiortuplo

#funcao que ordena os tuplos dentro de um tuplo, da menor para a maior len 

def ordena_tuplo(tuplo):
    tuplo = list(tuplo)     #transformamos o tuplo numa lista porque tuplos sao imutaveis
    nenhuma_troca = False
    while not nenhuma_troca:
        nenhuma_troca = False
        for i in range(len(tuplo) - 1):
            if len(tuplo[i]) > len(tuplo[i + 1]):
                nenhuma_troca = True
                tuplo[i], tuplo[i+1] = tuplo[i+1], tuplo[i]
    return tuple(tuplo)

#-------------------------------------------------------------------------------------------------------------
#--------------------------------TAD coordenada---------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

def cria_coordenada(l,c):
    if isinstance(l,int) and isinstance(c,int):
        if l>0 and c>0:
            return (l,c)
        else:
            raise ValueError ('cria_coordenada: argumentos invalidos')
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos')

def coordenada_linha(coordenada):
    return coordenada[0]

def coordenada_coluna(coordenada):
    return coordenada[1]

def e_coordenada(x):
    return isinstance(x[0],int) and isinstance(x[1],int) and x[0]>0 and x[1]>0 and len(x)==2

def coordenadas_iguais(x,y):
    if e_coordenada(x) and e_coordenada(y):
        if x[0]==y[0] and x[1]==y[1]:
            return True
        else:
            return False
    else:
        return False

def coordenada_para_cadeia(c):
    if e_coordenada(c):
        print('"'+'('+str(coordenada_linha(c))+':'+str(coordenada_coluna(c))+')'+'"')


#-------------------------------------------------------------------------------------------------------------
#--------------------------------------TAD Tabuleiro----------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

def cria_tabuleiro(t):
    if not len(t)==2 or not isinstance(t[0], tuple) or not isinstance(t[1], tuple) or len(t[0])!=len(t[1]):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    for i in t[0]:                 #percorremos o tuplo que constitui as linhas
        if not isinstance(i, tuple):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        
        for a in i:
            if not isinstance(a, int) or not a>0:
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            
    for l in t[1]:                 #percorremos o tuplo que constitui as colunas
        if not isinstance(l, tuple):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        
        for b in l:
            if not isinstance(b, int) or not b>0:
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            
    tabuleiro = []
    for el in range(len(t[1])):
        tabuleiro = tabuleiro + [[0]*len(t[1])]
    return [t[0]] + [t[1]] + [tabuleiro]




def tabuleiro_dimensoes(t):
    return (len(t[0]),len(t[1]))
    

def tabuleiro_especificacoes(t):
    return (t[0], t[1])

def tabuleiro_celula(t,c):
    if e_coordenada(c):
        x = c[0] - 1
        y = c[1] - 1
        z = t[2][x][y]
        if z == 0:
            return 0
        elif z == 1:
            return 1
        elif z == 2:
            return 2
    
def tabuleiro_preenche_celula(t,c,e):
    x = c[0] - 1
    y = c[1] - 1
    if e == 0:
        t[2][x][y] = 0
    elif e == 1:
        t[2][x][y] = 1
    elif e == 2:
        t[2][x][y] = 2
    else:
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos') 
    return t 
    
def e_tabuleiro(t):
    if len(t) == 3 and len(t[0]) == len(t[1]):      
        if isinstance(t[2], list):
            if isinstance(t[0], tuple) and isinstance(t[1], tuple):
                return True
    return False

#def tabuleiro_completo(
        
                
def tabuleiros_iguais(t1,t2):
    if e_tabuleiro(t1) and e_tabuleiro(t2):
        if t1==t2:
            return True
        else:
            return False
    else:
        return False 


def escreve_tabuleiro(t):
    for i in t[2]:        #Tabuleiro em si
        string = ''
        for e in i:
            if e == 0:
                string =string + '[ ? ]'
            elif e == 1:
                string = string + '[ . ]'
            else:
                string = string + '[ x ]'
        print(string)
            
        


#-------------------------------------------------------------------------------------------------------------
#--------------------------------------TAD Jogada-------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
