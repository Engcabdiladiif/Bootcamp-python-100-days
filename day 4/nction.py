# functions ptyhon

# block of code function waxaa logu tlao galay inuu qabto shqao goniya
# def ayaa functionka laga horaysiya

#basic function
# def my_function():
#     print("hellow world")
# my_function()


# hadadda doonayso in functionka waxbaa ku jirin
# pass
# def my_function():
#     pass

# argument   waana function lwh paramete

# def my_function(name):           # name ayaaa leh Argument
#     print("Asc",name)
# my_function("cabdiladiif")


# maths


# def add(x):
#     print(10  * x)
# add(5)

# multiple Argument

# def my_function(name,age):
#     print(f"magcaygu waa cabdiladiif da,dayduna waa {age}")
# my_function("cabdiladiif",22)


# Arbatirary Argument

# waa Argument aad adu iska u samaysatay waxna ku xidhayn
# data type uu isticmaal waa tubal

# def mykids(*kids):
#     print("waxaa guulayatay waa" + kids[0])
# mykids("cabdiladiif","sallax","Axmed")

# kan wuxuu Arbitary argument kaga duwan yahay umah bahnid wax idhex ah
# key word Argumment(kwarges)
#

#  Argument keyword

# def My_function(child1,child2):
#     print("my younges kid is " +child1)
# My_function("sakeriye","saalax")

# another Example Argument keyword

# def my_fuction(child1,child2):
#     print("my younges my baby is " + child1)
# my_fuction(child1 = "mohmed", child2= "yuusuf")

#  Arbitatury Argument keyword (** kwargs)

#waxaana loo isticmaal markanad odayn inta Argument aad so gelinayso marka
# call garaynayso
# dictionary lagu run gareeya

# def my_function(**kids):
#     print("my last name is " + kids["last_name"])
# my_function(first_name = "cabdiladiif", last_name = "axmed")


# return vaue


# waa waxay ku soo celiyaan informationka
# print waxaa loo isticmaal out functionka

# def  fun1(x):
#     return  5 + x
# print(fun1(10))

# multin using

# def my_function(x,y):
#     return x * y
# print(my_function(6,7))

# default parameter
 
 
# def wadan(wadan = "somali"):
#     print("iam form wadan " + wadan)
# wadan()

# lambda function / Expression - small ANONYMOUS FUNCTION
# waa function yaryar wana fucntion aan magca laahyn

#  lambada argument : expersyions

# x = lambda  a: a + 10
# print(x(5))
#

# multiple
# 
# x = lambda a, b: a * b
# print(x(9, 10))