class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #for sorted array above code works vwell
        '''l=0
        r=len(nums)-1
        while l<=r:
            s=nums[l]+nums[r]
            if s==target:
                return [l,r]
            elif s>target:
                r-=1
            else:
                l+=1'''
        # bruteforce
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
        # optimal 
        s={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in s:
                return [s[need],i]
            s[nums[i]]=i


                