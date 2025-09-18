def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return ValueError
    mn = -9e6 #-(9*10**6)
    mx = 9e6 #   9*10**6
    for i in range(len(nums)):
        if nums[i] < mn:
            mn = nums[i]
        if nums[i] > mx:
            mx = nums[i]
    return(tuple[mn, mx])

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = set(nums)
    return sorted(unique_nums)

def flatten(mat: list[list | tuple]) -> list:
    array = list()
    for arr in mat:
        if not (isinstance(arr, tuple) or isinstance(arr, list)):
            return TypeError
        for member in arr:
            array.append(member)
    return array

