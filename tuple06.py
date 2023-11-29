def main(tuple1):
    """
    A tuple of units and zeros with a length of five is given. Replace one with True.
    Args:
        tuple1 (tuple): parameter
    Returns:
        tuple: return answer
    """
    q=''
    for i in tuple1:
        if i==1:
            q+='True,'+' '
        elif i!=1:
            i=str(i)
            q+=i+', '
    return f'({q[:-2]})'


