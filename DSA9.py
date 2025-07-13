class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        from collections import Counter

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        freq = Counter(nums)

        for count in freq.values():
            if is_prime(count):
                return True
        return False
