# adding
# def add(a,b):
#     return a + b
# print(add(3,65))

# even or odd
# def checker(n):
#     if n % 2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(checker(2))

# square or not
# def sq(n):
#     return (n**2)
# print(sq(9))

# max num
# def lar(a,b,c):
#     return max(a,b,c)
# print(lar(2,4,2))

# factorial
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(30))

# reverse
# def str(n):
#     return n[::-1]
# print(str('pratik'))

# palindrom
# def pali(n):
#     n=n.lower()
#     return n == n[::-1]
# print((pali("dpd")))

# fibonacci
# def fibo(n):
#     if n ==0:
#         return[]
#     elif n ==1:
#         return[0]
#     elif n ==2:
#         return [0,1]
#     else:
#         seq=fibo(n-1)
#         seq.append(seq[-1]+seq[-2])
#         return seq
# print(fibo(9))

  

# tower of hanoi
# def hanoi(n,source,target,auxillary):
#     if n ==1 :
#         print(f"move disk {1} from {source} to {target}")
#         return 
#     hanoi (n-1,source,auxillary,target)
#     print(f"move disk {n} from {source} to {target}")

#     hanoi(n-1,auxillary,target,source)

# print(hanoi(3,'a','b','c'))