from DataStructures.List import array_list as lt

def default_compare_higher_value(father_node, child_node):
    if father_node['key'] >= child_node['key']:
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if father_node['key'] <= child_node['key']:
        return True
    return False

def new_heap(is_min_pq=True):
    heap = {}
    heap['elements'] = lt.new_list()
    heap['size'] = 0
    if is_min_pq:
        heap['cmp_function'] = default_compare_lower_value
    else:
        heap['cmp_function'] = default_compare_higher_value
    return heap

def size(my_heap):
    return my_heap['size']

def is_empty(my_heap):
    return my_heap['size'] == 0

def get_first_priority(my_heap):
    if my_heap['size'] == 0:
        return None
    return my_heap['elements']['elements'][1]['value']

def insert(my_heap, key, value):
    my_heap['size'] += 1
    my_heap['elements'].append({'key': key, 'value': value})
    swim(my_heap, my_heap['size'])


def remove(my_heap):
    if my_heap['size'] == 0:
        return None
    highest_priority_element = my_heap['elements']['elements'][0]['value']
    my_heap['elements']['elements'][0] = my_heap['elements']['elements'][my_heap['size'] - 1]
    my_heap['size'] -= 1
    my_heap['elements']['elements'] = my_heap['elements']['elements'][:my_heap['size']]
    index = 0
    while 2 * index + 1 < my_heap['size']:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < my_heap['size'] and my_heap['cmp_function'](my_heap['elements']['elements'][left], my_heap['elements']['elements'][smallest]) < 0:
            smallest = left
        if right < my_heap['size'] and my_heap['cmp_function'](my_heap['elements']['elements'][right], my_heap['elements']['elements'][smallest]) < 0:
            smallest = right
        if smallest != index:
            my_heap['elements']['elements'][index], my_heap['elements']['elements'][smallest] = my_heap['elements']['elements'][smallest], my_heap['elements']['elements'][index]
            index = smallest
        else:
            index = my_heap['size']
    return highest_priority_element




def swim(my_heap, pos):
    while pos > 1 and my_heap['elements']['elements'][pos - 1]['key'] < my_heap['elements']['elements'][pos // 2 - 1]['key']:
        my_heap['elements']['elements'][pos - 1], my_heap['elements']['elements'][pos // 2 - 1] = my_heap['elements']['elements'][pos // 2 - 1], my_heap['elements']['elements'][pos - 1]
        pos //= 2


def sink(my_heap, pos):
    while 2 * pos <= my_heap['size']:
        left_child = 2 * pos
        right_child = 2 * pos + 1
        smallest = pos
        if left_child <= my_heap['size'] and my_heap['elements']['elements'][left_child - 1]['key'] < my_heap['elements']['elements'][smallest - 1]['key']:
            smallest = left_child
        if right_child <= my_heap['size'] and my_heap['elements']['elements'][right_child - 1]['key'] < my_heap['elements']['elements'][smallest - 1]['key']:
            smallest = right_child
        if smallest == pos:
            return
        my_heap['elements']['elements'][pos - 1], my_heap['elements']['elements'][smallest - 1] = my_heap['elements']['elements'][smallest - 1], my_heap['elements']['elements'][pos - 1]
        pos = smallest
