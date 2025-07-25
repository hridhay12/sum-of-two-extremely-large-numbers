class Solution:
    import sys
    sys.set_int_max_str_digits(100000)
    def findSum(self, s1, s2):
        f=int(s1)
        g=int(s2)
        return str(f+g)

x=int(input("enter first number: "))
y=int(input("enter second number: "))
solution = Solution()
result = solution.findSum(str(x), str(y))
print("The sum is:", result)


