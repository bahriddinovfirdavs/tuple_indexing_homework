def main(tuple1):
    """
    A tuple of several elements is given. Return the first item.
    Args:
        tuple1 (tuple): parameter
    Returns:
        tuple: return answer
    """
    return tuple1[0]
tuple1=tuple(map(int,input().split()))
print(main(tuple1))