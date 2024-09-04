from . import list_node as node


def new_list():
    newlist={'first': None,
             'last': None,
             'size': 0}
    return newlist

def add_first(lista, elemento):
    new_nodo = node.new_single_node(elemento)
    new_nodo['next'] = None
    if lista["size"] == 0:
        lista['first'] = new_nodo
        lista['last'] = new_nodo
    else:
        new_nodo['next'] = lista['first']
        lista['first'] = new_nodo
    lista['size'] += 1
    return lista

def add_last(lista, elemento):
    new_nodo = node.new_single_node(elemento)
    if lista["size"] == 0:
        lista['first'] = new_nodo
        lista['last'] = new_nodo
    else:
        lista['last']['next'] = new_nodo
        lista['last'] = new_nodo
    lista['size'] += 1
    return lista

def is_empty(lista):
    return lista['size'] == 0
        
def size(lista):
    return lista["size"]

def first_element(lista):
    if lista["size"] == 0:
        return None
    else:
        return lista["first"]['info']
    
def last_element(lista):
    if lista['size'] == 0:
        return None
    else:
        return lista['last']['info']
    
def get_element(lista, pos):
    if is_empty(lista):
        return None
    if pos < 0 or pos >= lista['size']:
        return None
    current = lista['first']
    for _ in range(pos):
        current = current['next']
    return current['info']

def remove_first(lista):
    if lista['size'] == 0:
        return None
    first = lista['first']
    first_value = first['info']
    lista['first'] = first['next']
    if lista['size'] == 1:
        lista['last'] = None
    lista['size'] -= 1
    return first_value
    
def remove_last(lista):
    if lista['size'] == 0:
        return None
    current = lista['first']
    while current['next'] is not lista['last']:
        current = current['next']
    last = lista['last']['info']
    current['next'] = None
    lista['last'] = current
    lista['size'] -= 1
    return last

def insert_element(lista, element, pos):
    new_node = node.new_single_node(element)
    if pos < 0 or pos > lista['size']:
        return None
    if pos == 0:
        new_node['next'] = lista['first']
        lista['first'] = new_node
        if lista['size'] == 0:
            lista['last'] = new_node
        lista['size'] += 1
        return lista
    current = lista['first']
    for _ in range(pos - 1):
        current = current['next']
    new_node['next'] = current['next']
    current['next'] = new_node
    if new_node['next'] is None:
        lista['last'] = new_node
    lista['size'] += 1
    return lista

def is_present(lista, element, cmp_function):
    current = lista['first']
    pos = 0
    while current is not None:
        if cmp_function(current['info'], element) == 0:
            return pos
        current = current['next']
        pos += 1
    return -1

def delete_element(lista, pos):
    if pos < 0 or pos > lista['size']:
        return None
    if lista['size'] == 0:
        return None
    if pos == 0:
        deleted = lista['first']
        lista['first'] = deleted['next']
        if lista['size'] == 1:
            lista['last'] = None
        lista['size'] -= 1
        return lista
    current = lista['first']
    for _ in range(pos - 1):
        current = current['next']
    deleted = current['next']
    current['next'] = deleted['next']
    if deleted['next'] is None:
        lista['last'] = current
    lista['size'] -= 1
    return lista

def change_info(lista, pos, new_info):
    current = lista['first']
    for _ in range(pos):
        current = current['next']
    current['info'] = new_info
    return lista

def exchange(lista, pos1, pos2):
    if pos1 == pos2:
        return lista
    current = lista['first']
    node1 = None
    for _ in range(pos1):
        current = current['next']
    node1 = current
    current = lista['first']
    node2 = None
    for _ in range(pos2):
        current = current['next']
    node2 = current
    node1['info'], node2['info'] = node2['info'], node1['info']
    return lista

def sub_list(lista, pos, num_elem):
    lista_new = new_list()
    current = lista['first']
    for _ in range(pos):
        current = current['next']
    count = 0
    while count < num_elem:
        add_last(lista_new, current['info'])
        current = current['next']
        count += 1
    return lista_new