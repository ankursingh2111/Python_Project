def dict_operation():
    dict_list=dict()
    dict_mail=dict()
    filename=input("Enter the filename: ")
    filehandle=open(filename)
    for line in filehandle:
        if line.startswith('From'):
            list1=line.split()
            if len(list1)>2:
                    dict_list[list1[2]]=dict_list.get(list1[2],0) + 1
            if len(list1)>1:
                dict_mail[list1[1]]=dict_mail.get(list1[1],0) + 1
    print(dict_list)
    print(dict_mail)
    max=0
    for key in dict_mail:
        if max<dict_mail[key]:
            key_max=key
            max=dict_mail[key]
    print(key_max,":",dict_mail[key_max])    

dict_operation()
