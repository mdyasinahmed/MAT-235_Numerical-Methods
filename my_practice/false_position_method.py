def f(x):
    return x**3 - 4 * x - 9  # Define the given function


# Function to implement Regula Falsi Method
def regula_falsi(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses. The function must have opposite signs at a and b.")
        return None
   
    while True:
        # Calculate c using the Regula Falsi formula
        c = a - (f(a) * (b - a)) / (f(b) - f(a))
       
        # Compute f(c)
        f_c = f(c)
       
        # Check if the absolute value of f(c) is within the tolerance
        if abs(f_c) < tol:
            return c  # Approximate root found
       
        # Update the interval based on the sign of f(c)
        if f_c * f(a) < 0:
            b = c  # Root is in the left subinterval
        else:
            a = c  # Root is in the right subinterval


# Initial interval [a, b] and tolerance
a = 2
b = 3
tolerance = 0.0001


# Call the function and print the root
root = regula_falsi(a, b, tolerance)
if root is not None:
    print(f"The approximate root is: {root:.4f}")

