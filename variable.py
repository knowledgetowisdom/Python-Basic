#Variables are case sensitive 
x=6
X="knowledge"
print(x)
print(X)

#Casting of variable
p=str(8)
q=int(8)
s=float(8)
print(p)
print(q)
print(s)

#Get the type of a variable
print(type(p))
print(type(q))
print(type(s))

#single or double quotes both are same
a='apple'
b="apple"
print(a)
print(b)

#Valid variable name
my_var=2
_myvar=3
my2var=4
print(my_var)
print(_myvar)
print(my2var)

#invalid variable name
2my_var =5
#sybtaxError:invalid syntax

#assign many value to multiple variable
x,y,z="apple","mango","banana"
print(x)
print(y)
print(z)

#assign one value to multiple variable
i=j=k="apple"
print(i)
print(j)
print(k)

#unpack a collection in a list
fruits=["apple","mango","banana"]
w,u,v=fruits
print(w)
print(u)
print(v)

#output variable
x_="interesting"
print("Python is "+x_)

y_="Python is "
z_=y_+x_
print(z_)

#combine string and number gives an error
a_=5
b_="India"
c_=a_+b_
#TypeError:unsupported operand type(s) for +: 'int' and 'str'

#Global variable
p_="interesting"
def myfunc():
    print("Python is "+p_)
myfunc()

#Global vs local variable
q_="interesting"
def myfunc1():
    q_="very good"
    print("python is "+q_)
myfunc1()
print("Python is "+q_)

#global keyword
def myfunc2():
    global s_
    s_="interesting"
    print("Python is "+s_)
myfunc2()
print("python is "+s_)