class Solution(object):
    
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        out = []
        if type(nestedList) == int:
            out.append(nestedList)
            return out
        for iter in nestedList:
            if type(iter) == list:
                out.extend(self.flatten(iter))
            else:
                out.append(iter)

        return out

def main():
    inst = Solution()
    target = [1,2,[3,4],[5,[6,7]]]
    print inst.flatten(target)

if __name__ == '__main__':
    main()