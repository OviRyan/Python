def divide_elements(values, divisor):
    try:
        result = [value / divisor for value in values]
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Divisor must be a numeric value.")

# Example usage
values = [10, 20, 30, 40]
divisor = 0  # Test division by zero
print(divide_elements(values, divisor))

divisor = "a"  # Test non-numeric divisor
print(divide_elements(values, divisor))

divisor = 5  # Test valid divisor
print(divide_elements(values, divisor))
