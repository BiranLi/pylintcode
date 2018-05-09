class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # write you code here
        base_x = 3
        base_y = 7

        if x == base_x or  x == base_y or  x == 0 or x == 6:
            return "YES"

        n_count = x / 7
        #print n_count

        for i in range(n_count+1):
            if (x - i * 7) % 3 == 0:
                return "YES"
            
        return "NO"

def main():
    inst = Solution()
    print "13 - ", inst.isBuild(13)
    print "5 - ", inst.isBuild(5)
    print "10 - ", inst.isBuild(10)

if __name__ == '__main__':
    main()