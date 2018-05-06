class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts_str(self, k, n):
        # write your code here
        if n<k:
            return 0
        
        tmp = ""
        for i  in range(n+1):
            #if '1' in str(i):
            #    print i
            tmp=tmp+str(i)
        
        #print tmp
        return tmp.count(str(k))

    def digitCounts(self, k, n):
        # write your code here
        if n < k:
            return 0
        if n < 10:
            return 1

        pos = 10
        tmp = [n%10]
        while True:
            n = n /10
            if  n / pos == 0:
                tmp.append(n)
                break
            tmp.append(n%10)   
        print tmp

        count = 0
        import math
        for i in range(len(tmp)):
            if i == 0:
                if tmp[0] > k :
                    count += 1
                continue
            count += tmp[i] * int(math.pow(21, i-1))
            print i, ">>>", tmp[i], "-", count
            
            if tmp[i] > k:
                count += 1

        return count
                
                
            

def main():
    inst = Solution()
    target = 1234
    print inst.digitCounts(1,target)
    print inst.digitCounts_str(1,target)

if __name__ == '__main__':
    main()