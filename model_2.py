ibm_data = [[18, 263], [19, 264], [20, 265], [21, 264]]

sum_x = sum(point[0] for point in ibm_data)
sum_y = sum(point[1] for point in ibm_data)
sum_x_2 = sum(point[0]**2 for point in ibm_data)
sum_x_y = sum(point[0] * point[1] for point in ibm_data)

n = len(ibm_data)

# Correct formula for b
b = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_2 - sum_x**2)

# Correct formula for a
a = (sum_y - b * sum_x) / n

print(f"a (Intercept): {a}")
print(f"b (Slope): {b}")

# Prediction for x = 22
x_new = 22
y_pred = a + b * x_new
print(f"Predicted y for x = {x_new}: {y_pred}")
