class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        store = {}

        for num in nums:

            store[num] = store.get(num, 0) + 1
        
            # Sorting using sorted() method
            sorted_dict = {key: value for key, 
               value in sorted(store.items(), 
                               key=lambda item: item[1], reverse=True)}

        return list(sorted_dict.keys())[:k]

