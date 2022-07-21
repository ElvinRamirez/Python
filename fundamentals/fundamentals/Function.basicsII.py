#1 Countdown 
def countdown(num):
    x = []
    for i in range(num,-1,-1):
        x.append(i)
    return x

print(countdown(25))

#2 Print and Return 
def print_and_return(y):
    print(y[0])
    return y[1]

print(print_and_return([5,6]))

#3First Plus Length
def print_and_sum(z):
    return z[0]  + len(z)

print(print_and_sum([1,2,3,4,5,6,7,8,9]))

#4 Values Greater than Second
def greater_than(num):
    p = [] 
    if len(num) < 3: #if the list in the argument has less than 2 elements, will return False
        return False
    for i in range(len(num)):
        if num[i] > num[1]:
            p.append(num[i])
    print(len(p)) #prints how many numbers are greater than the second index of the list
    return p #prints the list of numbers thatr are greater than the second index

print(greater_than([8,3,2,4,1,7,]))
print(greater_than([4]))

#5 This Length, That Value 
#parameters = 2 integers,size(length) and value equal to the integer used for size
#create an empty list and return this values 
def this_that(a,b):
    value = []
    for i in range((a)):
        i = b
        value.append(a*[i])
        return value

print(this_that(3,8))
print(this_that(5,3))
