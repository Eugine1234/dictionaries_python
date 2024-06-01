#Dctionary_nesting

student_grades = {}
for student in 'student_score':
    score = 'student_score'[student]
    if score > 90:
        student_grades[student] = "outstanding"
    
    elif score > 80:
     student_grades[student] = 'Excel'
     Exception
    elif score > 70:
     student_grades[student] = 'Acceptable'
    else:
        print(student_grades)
        
        #list_duplicate
        g = [11, 34, 56, 45]
        h = [45, 78, 98, 90]
        print (g, h, 'len(g)' 'type(g)')
        print(g[3])
        print(g[2])
        if 2 in g:
            print('true')
        else:
            print('false')
            g[1] = 34569565
            
            print(g)
              
              
              #append.() method
    a = [1,3,4,5,6,7,8]
    a.append('string')
    print(a)
            #insert method
    b = [1,3,4,5,6,7,8]
    b.insert(1, 'string')
    print(b)
            
            
            #extend method
    c = [1,3,4,5,6,7,8,]
    d = ['string']
    c.extend(0)
    print(c)
    
    #removing method
    a = [1,3,4,5,6,7,8]
    a.remove(4)
    print(a)
    
    #pop method
    b = [11,13,14,15,16]
    b.pop(3)
    print(b)
    c = [1,3,4,5,6,7,8,]
    del[2]
    print(c)
    
    #clear method
    c = [1,3,4,5,6,7,8]
    c.clear(3)
    print(c)
    
    #list comprehension
    a = ['1','3','4','5','6','7']
    b = []
    for x in a:
        b.append(x)
        print(b)
        
        
        #sorting of list
        d = [1,34,567,876]
        print(d)
        d.sort(c)
        print(d)
        
        #copying
        
        d = [1,3,4,5,6,7,8,9]
        d.copy()
        print(d)
        print(d)
        f = list (d)
        print(f)
        g = f+d
        print(g)
        
        #turple immutable
        d = (1,3,4,5,6,7,8,9)
        d = list (d)
        d.insert(1,'string')
        e = [1,3,4,5,6,7,8,9]
        d.extend(e)
        d.append(8)
        d.remove(4)
        d.pop(5)
        d = 'turple'(d)
        print(d)
        
        
        #set
        q = {}
        w = {1,3,4,5,6,7,8,9}
        x = {'string', 12, 12.78, 12j}
        print(q, type(q, len(q)))
        print(w, type(w), len(w))
        print(x, type(x), len(x))
        


            
        
