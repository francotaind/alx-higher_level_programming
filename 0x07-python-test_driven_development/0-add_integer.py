def add_integer(a, b=98):
    #check if a and b are intergers or foats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b

# Example usage:
result = add_integer(5, 3.5)
print(result)  # Output: 8
