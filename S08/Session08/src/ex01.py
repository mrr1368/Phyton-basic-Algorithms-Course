

def function_name():
    num1 = 2 
    num2 = 5

    print(num1 * num2)

# ---------------------------------------

# ورودی ندارد خروجی ندارد

def function_name():
    num1 = 2 
    num2 = 5

    print(num1 * num2)

function_name(2, 5)

function_name()
function_name()
function_name()

# ---------------------------------------

# ورودی دارد خروجی ندارد

def function_name(num1, num2):

    print(num1 * num2)

function_name(2, 5)
function_name(7, 3)
function_name(4, 6)

data1 = int(input("num1 :"))
data2 = int(input("num1 :"))

function_name(data1, data2)

# ----------------------------------------

# ورودی دارد خروجی دارد

def function_name(num1, num2):

    res = num1 * num2
    return res

n1 = int(input("n1 :"))
n2 = int(input("n2 :"))

data1 = function_name(2, 5)
data2 = function_name(3, 9)
data3 = function_name(n1, n2)

# ----------------------------------------

# ورودی ندارد خروجی دارد

def get_pi():
    return 3.1456789

res = get_pi()
