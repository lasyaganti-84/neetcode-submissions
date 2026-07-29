class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapnum = {}
        for i, num in enumerate(nums):
            if num in mapnum and i - mapnum[num] <= k:
                return True
            
            mapnum[num] = i

        return False

