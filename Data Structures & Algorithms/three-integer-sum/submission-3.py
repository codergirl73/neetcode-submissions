class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sort_nums = sorted(nums)
        print(sort_nums)
        i=0
        while i < len(sort_nums):

            if i>0 and sort_nums[i] == sort_nums[i-1]:
                i+=1
                continue


            target = -sort_nums[i]
            left = i+1
            right = len(nums)-1
            
            while left<right:
                res_inside = []
                if sort_nums[left] + sort_nums[right] == target:
                    res_inside.append(sort_nums[i])
                    res_inside.append(sort_nums[left])
                    res_inside.append(sort_nums[right])
                    if len(res_inside)!=0:
                        res.append(res_inside)

                    left+=1
                    right-=1
                    while left<right and sort_nums[left] == sort_nums[left-1]:

                        left += 1
                    while left<right and sort_nums[right] == sort_nums[right+1]:

                        right-=1
                
                elif sort_nums[left] + sort_nums[right] < target:
                    left+=1
                else:
                    right-=1
                
 
            
           
            i+=1
        
        return res





