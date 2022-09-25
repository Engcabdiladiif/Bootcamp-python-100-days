# function and input

# 002 function and input

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
# format_name("cabdiladiif", "SAALAX")

# def format_name(f_name, l_name):
#     formadted_f_name = f_name.title()
#     formadted_l_name = l_name.title()
#     print(f"{formadted_f} {formadted_l}")
# format_name("Abdiladiif", "AxmeD")


# another same return value


# def format_name(f_name, l_name):
#     formadted_f_name = f_name.title()
#     formadted_l_name = l_name.title()
#
#     return  f"{formadted_f_name} {formadted_l_name}"
# formated_string = format_name("cabdiladiif" ,"Saalax")
# print(formated_string)

# # or same
#
# def format_name(f_name, l_name):
#     formadted_f_name = f_name.title()
#     formadted_l_name = l_name.title()
#     return f"{formadted_f_name} {formadted_l_name}"
# print(format_name("cabdiladiif", "saalax"))


# # 003 multi return value
# def format_name(f_name, l_name):
#    formadted_f_name = f_name.title()
#    formadted_l_name = l_name.title()
#    return f"{formadted_f_name} {formadted_l_name}"
# print(format_name(input("what is yor name fisrt name"),
# input("what is your laste name")))

# 004 code challenge day in month

# def is_leap(year):
#    if year %4 == 0:
#       if year %100 == 0:
#          if year % 400 == 0:
#             return True
#          else:
#             return False
#       else:
#          return True
#    else:
#       return False
#
# def days_in_month(year, month):
#    month_days = [31,28,31,30,31,31,34]
#    if is_leap(year) and month == 2 :
#       return  29
#    return month_days[month - 1]
#
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)

# 005 Docstrings

# def my_function(num1,  num2):
#    '''
#    sidaas weye.
#    '''
#
#    return num1 ** num2
#
# print(my_function(2, 2))
# print(my_function.__doc__)

# # 007 creating calculator

def add(n1, n2):
   return n1 + n2

#substract

def subtract(n1, n2):
   return n1 - n2

# multiple

def multiple(n1,n2):
   return  n1 * n2

# Divided

def divide(n1, n2):
   return  n1 / n2
apperation = {

   "+": add,
   "-": subtract,
   "*":multiple,
   "/":divide,
}

# function = apperation["+"]
# function(2, 3)



num1 = int(input("what is the first number: " ))
for symbol in apperation:
   print(symbol)

operation_symbol =input("pick an operaion from the line above:")
num2 = int(input("what is the second number: "))
caculation_function = apperation[operation_symbol]
answer = caculation_function(num1, num2)

print(f" {num1}{operation_symbol} {num2} = {answer}")
