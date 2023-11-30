def main(tuple1):
    """
    A tuple of several elements is given. True if all items are the same, otherwise return False.
    Args:
        tuple1 (tuple): parameter
    Returns:
        bool: return answer
    """
    q=0
    w=0
    for i in tuple1:
        if i==q:
            q=i
            w+=1
    if len(tuple1)== w:
        return True
    else:
        return False
   
        
    