from . import list_node as node


def new_list():
    newlist={'first': None,
             'last': None,
             'size': 0}
    return newlist

def add_first(lista, elemento):
    new_nodo = node.new_single_node(elemento)
    print(new_nodo)
    if lista["size"] == 0:
        lista['first'] = new_nodo
        lista['last'] = new_nodo
        lista["size"] += 1
        print(lista)
        return lista
    else:
        lista['next'] = lista['first']
        lista['first'] = new_nodo
        lista["size"] += 1
        print(lista)
        return lista
'''
lista_aja = new_list()
add_first(lista_aja, 1)
add_first(lista_aja, 2)
add_first(lista_aja, 3)
print(lista)'''

def add_last(lista, elemento):
    new_nodo =node.new_single_node(elemento)

    if lista["size"] == 0:
        new_nodo['first'] = new_nodo
        new_nodo['last'] = new_nodo
        return lista
    
    else:
        lista['last'] = new_nodo
        return lista

        
def size(lista):
    return lista["size"]

def first_element(list):
    if list["size"] == 0:
        return None
    else:
        return list["first"]