"""Linear Regression"""

ibm_data= [[18,263],[19,264],[20,265],[21,264]]
#a= [sum(y)*sum(x**2)-sum(x)sum(x*y)]/[len(arr)sum(x**2)-sum(x)**2]
n=len(ibm_data)
sum_y =0
for i in range(0,n):
    sum_y+=ibm_data[i][1]
print(sum_y)

sum_x = 0
for i in range(0,n):
    sum_x+=ibm_data[i][0]
print(sum_x)

sum_x_2 = 0
for i in range(0,n):
    sum_x_2+=ibm_data[i][0]**2   
print(sum_x_2)

sum_x_y=0
for i in range(0,n):
    sum_x_y+=ibm_data[i][1]*ibm_data[i][0]

print(sum_x_y)


a = ((sum_y * sum_x_2) - (sum_x * sum_x_y)) / ((n * sum_x_2) - (sum_x ** 2))
print(a)

#b= [len(arr)*(sum_x_y)-sum(x)sum(y)]/[len(arr)sum(x**2)-sum(x)**2]
b = ((n * sum_x_y) - (sum_x * sum_y)) / ((n * sum_x_2) - (sum_x ** 2))
print(b)

y= a+b*22
print(y)





