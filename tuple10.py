def main(tuple_num):
    """
    A tuple of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        tuple_num (tuple): parameter
    Returns:
        int: return answer
    """
    if tuple_num[0]>tuple_num[-1]:
        return tuple_num[0]
    if tuple_num[0]<tuple_num[-1]:
        return tuple_num[1]
    