#### basically make this into more features for every post: Hangye | Themes | Policy Type

@numba.jit(nopython=True)
def classify_policy(policy):
    """
    Helps classify a policy in terms of Industry, Themes, Policy_Type, tighten, Expand
    :param policy: raw chinese text or document.
    :returns: content describing the input policy in terms of Industry, Themes, Policy_Type, tighten, Expand
    """
    match = lambda a, b: [ b.index(x)+1 if x in b else None for x in a ]

    aa = []
    hangye_list = []
    temp = []
#for pol in policy:
    b = get_chinese_words(policy)
    Mylist = match(b,Hangye) # numbers reflect on nth element of 'Hangye'
    if len([e for e in Mylist if e != None]) == 0:
        hangye_list.append(None)
    else:
        for i in Mylist:
            if i is not None:
                aa.append(int(i))
                for j in aa:
                    if j is not None:
                        temp.append(Hangye[j-1])
        hangye_list.append(temp)  # why -1? 
                        # bc query from the real array, 0 index = 1 index
#print(len(hangye_list))

    bb = []
    themes_list = []
    temp = []
    #for pol in policy:
    b = get_chinese_words(policy)
    Mylist = match(b,Themes) # numbers reflect on nth element of 'Hangye'
    if len([e for e in Mylist if e != None]) == 0:
        themes_list.append(None)
    else:
        for i in Mylist:
            if i is not None:
                bb.append(int(i))
                for j in bb:
                    if j is not None:
                        temp.append(Themes[j-1])
        themes_list.append(temp) 
#print(len(themes_list))   

    cc = []
    type_list = []
    temp = []
    #for pol in policy:
    b = get_chinese_words(policy)
    Mylist = match(b,types_policy) # numbers reflect on nth element of 'Hangye'
    if len([e for e in Mylist if e != None]) == 0:
         type_list.append(None)
    else:
        for i in Mylist:
            if i is not None:
                cc.append(int(i))
                for j in cc:
                    if j is not None:
                        temp.append(types_policy[j-1])
        type_list.append(temp)             
#print(len(type_list))


    dd = []
    control_list = []
    temp = []
    #for pol in policy:
    b = get_chinese_words(policy)
    Mylist = match(b,tighten_control) # numbers reflect on nth element of 'Hangye'
    if len([e for e in Mylist if e != None]) == 0:
        control_list.append(None)
    else:
        for i in Mylist:
            if i is not None:
                dd.append(int(i))
                for j in dd:
                    if j is not None:
                        temp.append(tighten_control[j-1])
        control_list.append(temp)
#print(len(control_list))

    ee = []
    expand_list = []
    temp = []
    #for pol in policy:
    b = get_chinese_words(policy)
    Mylist = match(b,implement_expand) # numbers reflect on nth element of 'Hangye'
    if len([e for e in Mylist if e != None]) == 0:
        expand_list.append(None)
    else:
        for i in Mylist:
            if i is not None:
                ee.append(int(i))
                for j in ee:
                    if j is not None:
                        temp.append(implement_expand[j-1])
        expand_list.append(temp)
    #print(len(expand_list))
    print("Industry:", hangye_list,"\n"
          "Themes:", themes_list,"\n"
          "Policy Type:", type_list,"\n"
          "Policy Tighten:", control_list,"\n"
          "Policy Expansion:", expand_list)
