# 模板
# test case: [1,1,1,0,1] 和 [1,0,1,1,1] 和 [1]
def binarySearch(self, nums, target):
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
    # 在 first position == target 的情况下不会出现死循环
    # 但是在 last position == target 的情况下会出现死循环
    # 样例：nums=[1，1] target = 1
    # 为了统一模板，就都采用 start + 1 < end，可以保证不会出现死循环
    while start + 1 < end:
        # 利用两个while loop来去重
        '''
        while left + 1 < right and nums[left + 1] == nums[left]:
            left += 1
        while left + 1 < right and nums[right - 1] == nums[right]:
            right -= 1
        '''
        
        # python 没有 stack overflow 的问题，直接 // 2 就可以了
        # java和C++ 最好写成 mid = start + (end - start) / 2
        # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 stack overflow
        mid = start + (end - start) // 2
        
        # ！！！这一部分在比较的时候先考虑和end比较：如果用的< nums[start]的话，若整个数组只是单增没有rotated，那根本找不到一个< nums[start]的数，则会出现无解的问题
        # 直接去想什么情况要把 l = mid 或者 r = mid，想其中一边，然后剩下的用else就可以了
        # > , =, < 的逻辑分开思考，考虑清楚 = 的情况是否能合并到其他分支里
        if nums[mid] == target:
            return ...
        if nums[mid] < target:
            # 写作 start = mid + 1 也是正确的
            # 只是可以偷懒不写，因为不写也没问题，不会影响时间复杂度
            # 不写的好处是，万一你不小心写成了 mid - 1 你就错了
            start = mid
        else:
            # 同理,写作 end = mid - 1 也是正确的
            end = mid

    # 因为上面的循环退出条件是 start + 1 < end
    # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
    # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
    # 如果是找 first position of target 就先看 start，否则就先看 end
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end

    return -1
