def find_duplicate(nums):

    # bad approach
    # for num in nums:
    #     found = 0
    #     for num2 in nums:
    #         if num == num2:
    #             found += 1
    #         if found == 2:
    #             return num

    print(nums)
    nums.sort()

    for i, num in enumerate(nums):

        if num == nums[i+1]:
            return num

    print(nums)


print(find_duplicate([2, 3, 1, 3, 4]))
