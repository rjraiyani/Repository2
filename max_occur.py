import sys

def max_consecutive_ones(nums):
#    "Find the maximum number of consecutive 1s"
#    pass #TODO: Replace pass with your code


    max_occur = 0
    ctr = 0
    for i in nums:
        if i == 1:
            ctr += 1
            max_occur += 1
        elif i == 0:
            ctr = 0
            max_occur = 0
    print(max_occur)
    return
nums = map(int, sys.stdin.readline().split())

print(max_consecutive_ones(nums))
