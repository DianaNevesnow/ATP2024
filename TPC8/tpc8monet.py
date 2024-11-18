## tpc1
### a)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]  
ncommon = [n for n in list1 + list2 if (n in list1) != (n in list2)]

### b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
list = [word for word in texto.split(" ") if len(word)>3]

### c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i+1, lista[i]) for i in range(len(lista))]

## tpc2
### a)
def strCount(s, subs):
    count = 0
    i = 0
    while i <= len(s) - len(subs):
        if s[i:i+len(subs)] == subs:
            count += 1
            i += len(subs)
        else: 
            i += 1
    return count

### b)
def produtoM3(lista):
    biglist = sorted(lista)
    return biglist[0]*biglist[1]*biglist[2]

### c)
def reduxInt(n):
    while n >= 10:
        add = 0
        for cypher in str(n):
            add += int(cypher)
        n = add
    return n

### d)
def myIndexOf(s1, s2):
    i = 0
    res = -1
    while i <= len(s1) - len(s2):
        match = True
        for j in range(len(s2)):
            if s1[i + j] != s2[j]:
                match = False
                j = len(s2)  
        if match:
            return i  
        i += 1
    return res


## tpc3
### a)
def quantosPost(socialmedia):
    return len(socialmedia)

### b)
def postsAutor(socialmedia, op):
    list = []
    for post in socialmedia:
        if op == post["autor"]:
            list.append(post)
    return list

### c)
def autores(socialmedia): #terceira chave
    list=[]
    for post in socialmedia:
        if "autor" in post:
            list.append(post["autor"])
    return  list

### d)
def insPost(socialmedia, conteudo, op, dataCriacao, comment):
    id = f"p{len(socialmedia)+1}"
    post = {"id" : id, "conteudo" : conteudo, "autor" : op, 'dataCriacao': dataCriacao, 'comentarios': comment}
    return socialmedia.append(post)

### e)
def remPost(socialmedia, id):
    socialmedia = [post for post in socialmedia if post["id"] != id]
    return socialmedia

### f)
def postsPorAutor(socialmedia):
    distrib = {}
    for post in socialmedia:
        op = post.get("autor")
        if op in distrib:
            distrib[op] += 1
        else:
            distrib[op] = 1
    return distrib

### g)
def comentadoPor(socialmedia, op):
    list = []
    for post in socialmedia:
        if "comentarios" in post:
            for comment in post["comentarios"]:
                if comment.get("autor") == op:
                    list.append(post)
    return list

