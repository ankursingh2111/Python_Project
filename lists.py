def middle(temp_list):
    t_list=temp_list
    del t_list[0]
    del t_list[-1]
    print(t_list)
    return t_list
def chop(temp_list):
    t_list=temp_list[:]
    del t_list[0]
    del t_list[-1]
    print(t_list)

list1=[1,2,5,6,7,8]
middle(list1)
print(list1)
chop(list1)
print(list1)
