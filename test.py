def append_list():
    list.append('小毛')

def assign_list():
    list = ['嘿几把小毛']

def assign_list_returned(list):
    list = ["小毛嘿几把"]
    return list

list = ['嘿', '几', '吧']
print(list)

append_list()
print(list)

assign_list()
print(list)

list2 = assign_list_returned(list)
print(list2)