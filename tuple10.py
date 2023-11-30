def main(tuple_num):
    """
    A tuple of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        tuple_num (tuple): parameter
    Returns:
        int: return answer
    """
    a=tuple_num[0]
    b=tuple_num[-1]
    if a>b:
        return a
    if a<b:
        return b
