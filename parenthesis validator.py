
           
paren=input("enter brackets: ")

def calpos(paren):
    collect=[]
    count=0
    c=0
    for i in paren:
        c+=1
        if(paren[0]==']' or paren[0]=='}' or paren[0]==')'):
            count+=1
            return print('Validate at pos : ',count)
        if(i=='[' or i=='{' or i=='('):
            count+=1
            collect.append(i)
            continue
        collect.append(i)
        x=collect.pop()
        if(len(collect)!=0):
            y=collect.pop()
            if(x==']' and y=='['):
                count+=1
            elif(x=='}' and y=='{'):
                count+=1
            elif(x==')' and y=='('):
                count+=1
            else:
                count+=1
                return print('Validate at pos : ',count)
        else:
                count+=1
                return print('Validate at pos : ',count)
                          
           
    if(len(collect) != 0):
        l=collect.pop()
        if(l=='[' or l=='{' or l=='('):
            count+=1
    return print('Validate at pos : ',count)
        
            
        
    print(collect)
    print(count)
calpos(paren)