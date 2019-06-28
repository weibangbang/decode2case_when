#处理头元素包含的左括号"("
def head_handle(str):
    return str.split("(")[1]

#处理尾元素包含的右括号")"
def tail_handle(str):
    str_list=list(str)
    str_list.reverse()
    
    str_rever=''.join(str_list)
    index=str_rever.find(")")
    #用“#”号占个位置 分割decode 内外部元素
    str_rever_replace=str_rever[0:index]+"#"+str_rever[index+1:]
    str_rever_replace_list=list(str_rever_replace)
    str_rever_replace_list.reverse()
    return ''.join(str_rever_replace_list)

#用栈处理括号匹配
stack = []
#用数组保存decode内部元素
worls = []

#测试例子
#b_str="decode(name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(conact(a,b),conact(a,b)),'mid',b,c,d,eeee,colles(cast(cast('0' as int) as varchar),''),'lala')  as   name"
#b_str="decode(name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(conact(a,b),conact(a,b)),'mid',b,c,d,eeee,colles(cast(cast('0' as int) as varchar),''),'lala') "
#b_str="name,'Tom',cast(cast('0' as int) as varchar),'Anna',conact(a,b),'mid',b,c,d,eeeee"
#b_str="decode(cols,1,'male',0,'female')"
b_str="decode(cols,1,'male',0,'female','unkown')"
#把字符串拆分成字符
list(b_str)

st=''
#主要处理逻辑   拆散decode内部元素，放入数组中
for x in b_str:
    #遇到左括号入栈
    if x=='(':
        stack.append(x)
    #遇到右括号出栈
    elif  x==')':
        stack.pop()
    #遇到逗号，并且栈内元素为1，就判定 st 保存了decode内部一个完整元素的信息
    elif  x == ',' and len(stack)==1:
        worls.append(st)
        st=''
        x=''
    st+=x
worls.append(st)   

#调用处理头元素括号后覆盖数组中的旧的头元素
heald=head_handle(worls[0])
worls[0]=heald

#调用处理尾元素括号后覆盖数组中的旧的尾元素，如果有别名则做对应处理
tail=tail_handle(worls[-1])
#判断是否有别名
alias=''
if "#" in tail:
    worls[-1]=tail.split("#")[0]
    alias=tail.split("#")[1]


lengths=len(worls)

value=worls[0]
case_str='case '

    
index=0
while index<lengths-2:

    index+=2
    case_str+=" when "+value+"="+worls[index-1] +" then "+ worls[index]
    
if lengths%2==0:
    case_str+="else "  +  worls[-1]+" end "+alias
else:
    case_str+="else "  + "''"+" end "+alias
print(case_str)
