class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        comp = 0
        for i in range(len(nums)):
            print(nums[(i)])
            comp  = target - nums[(i)]
            print(comp)
            for j in range(len(nums)):

                
                if nums[(j)] == comp:
                    if i == j:
                        continue
                    return [i,j]
                    print(i,j)





        