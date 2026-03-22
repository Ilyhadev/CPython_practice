def dot_product(a, b):
    """Computes the dot product of two vectors in pure Python"""
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
