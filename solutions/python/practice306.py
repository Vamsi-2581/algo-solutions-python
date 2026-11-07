# Sum of All Odd Length Subarrays
# Problem: Sum of All Odd Length Subarrays
# Source: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Note: Calculates the sum of all contiguous subarrays having odd lengths.
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        n = len(arr)
        t = sum(arr)
        
        for i in range(n - 1):
            for j in range(i + 2, n, 2):
                temp = arr[i:j+1]
                print(temp)
                if len(temp) % 2 != 0:
                    t += sum(temp)

        return t
        
s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(s.sumOddLengthSubarrays([10,11,12]))  # 66
print(s.sumOddLengthSubarrays([1,2]))       # 3
# Test cases
assert s.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
assert s.sumOddLengthSubarrays([1, 2]) == 3
assert s.sumOddLengthSubarrays([10, 11, 12]) == 66
assert s.sumOddLengthSubarrays([]) == 0
assert s.sumOddLengthSubarrays([0, 0, 0]) == 0
assert s.sumOddLengthSubarrays([-1, 2, -3]) == -4
