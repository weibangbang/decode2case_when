#处理头元素包含的左括号"("
def head_handle(str):
    return str.split("(")[1]

#处理尾元素包含的右括号")"
def tail_handle(str):
    str_list=list(str)
    str_list.reverse()
    
    str_rever=''.join(str_list)
    index=str_rever.find(")")
    str_rever_replace=str_rever[0:index]+"#"+str_rever[index+1:]
    str_rever_replace_list=list(str_rever_replace)
    str_rever_replace_list.reverse()
    return ''.join(str_rever_replace_list)

#用栈处理括号匹配
stack = []
#用数组保存decode内部元素
worls = []

#测试用例
#b_str="decode(name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(conact(a,b),conact(a,b)),'mid',b,c,d,eeee,colles(cast(cast('0' as int) as varchar),''),'lala')  as   name"
b_str="decode(name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(conact(a,b),conact(a,b)),'mid',b,c,d,eeee,colles(cast(cast('0' as int) as varchar),''),'lala') "
#b_str="name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(a,b),'mid',b,c,d,eeeee"

#把字符串拆分成字符
list(b_str)

st=''
#主要处理逻辑   拆散decode内部元素，放入数组中
for x in b_str:
    #stack.append(x)
    #print(x)
    if x=='(':
        stack.append(x)
    elif  x==')':
        stack.pop()
    elif  x == ',' and len(stack)==1:
        worls.append(st)
        st=''
        x=''
    st+=x
worls.append(st)   

#处理头元素括号后覆盖数组中的旧的头元素
heald=head_handle(worls[0])
worls[0]=heald

#处理尾元素括号后覆盖数组中的旧的尾元素
tail=tail_handle(worls[-1])
alias=''
if "as" in tail:
    worls[-1]=tail.split("#")[0]
    alias=tail.split("#")[1]


lengths=len(worls)
print("lengths:"+str(lengths))
value=worls[0]
case_str='case '

    
index=0
while index<lengths-2:

    index+=2
    case_str+=" when "+value+"="+worls[index-1] +" then "+ worls[index]
case_str+="else "  +  worls[-1]+" end "+alias
print(case_str)
