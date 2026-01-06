squares_dict = {}

def key_val_squares_dict(n):
    for i in range(1, n + 1):
        key = i
        value = i ** 2
        squares_dict[key] = value
    return squares_dict
    
n = int(input())    
squares_dict = key_val_squares_dict(n)
print(squares_dict)