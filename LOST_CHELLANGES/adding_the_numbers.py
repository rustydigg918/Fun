    """Question:
    GET THE RECURSIVE SUM OF DIGITS INTO ONE DIGITS
    i/p- 14432, 987, 3345,2
    o/p- 5, 6, 6, 2
    """
    
    """MY SOLUTION
    def digital_root(n):
        _tokens = [int(i) for i in str(n)]
    _sum = sum(_tokens)
    if len(str(_sum)) > 1:
        _sum = digital_root(_sum)
    return _sum
    """
    
    """
    MY OPPOSITION CODE CODE
    def digital_root(n):
        return n%9 or n and 9
    """