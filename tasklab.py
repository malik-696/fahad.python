# def fun():
#     price=2000;
#     tax=15;
#     tax_amount = price *(tax/100)
#     final_price = tax_amount+price
#     return final_price
# print(fun());

# task 2:
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fac(n-1)
# number = int (input("enter a number to find its factorial"));
# print(fac(number))

# task 3

# def fun(tem):
#     if tem<10:
#         return "cold"
#     elif 10<= tem <=25:
#         return "warm"
#     else:
#         return "hot"
# user_input = int(input('enter temperature'));
# print(fun(user_input))

# task 4
# def fun(a,b):
#     sum= a+b
#     diff= a-b
#     prod= a*b
#     return sum,diff,prod
    
# x= int(input('Enter first number'))
# y= int(input('Enter second number'))
# s,d,p = fun(x,y)
# print('sum',s)
# print('diff',d)
# print('prod',p)

# task 5
def sum(value):
    total = 0
    for v in value:
        total += v
    return total
num = [2,5,8,10]
print('sum of list:',sum(num))