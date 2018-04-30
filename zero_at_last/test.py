class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        if n==0:
            return 1
        n_zero = 1
        while n/5 != 0:
            n = n/5
            n_zero += n
        return n_zero - 1   

def main():
    inst = Solution();
    print inst.trailingZeros(25)

if __name__ == '__main__':
    main()        
        
        