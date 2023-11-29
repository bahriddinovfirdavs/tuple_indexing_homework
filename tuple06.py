def main(tuple1):
    """
    A tuple of units and zeros with a length of five is given. Replace one with True.
    Args:
        tuple1 (tuple): parameter
    Returns:
        tuple: return answer
    """
    q=0
    for i in tuple1:
        q+=1
        if i==1:
            tuple1[q] = True
tuple1=(1,0,0,0,1)
print(main(tuple1)) 


