# second version
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    idx1 = 0
    idx2 = 0
    answer = []
    
    for i, a in enumerate(nums[:-1]):
        # print(f'Outer Loop : i: {i} / a: {a}')
        for j, b in enumerate(nums[i + 1:]):
            # print(f'Inner Loop : j: {j} / b: {b}')
            if a + b == target:
                idx1 = i
                idx2 = j + 1
                answer.append(i)
                answer.append(j + i + 1)
                return answer

    return [idx1, idx2]