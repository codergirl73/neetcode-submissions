class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        store = {}
        store_2 = {}

        if len(s) != len(t):

            return False
        
        else:
            for i in s:

                if i in store.keys():

                    store[i] +=1
                else:
                    store[i] = 1
            for i in t:
                if i in store_2.keys():

                    store_2[i] +=1
                else:
                    store_2[i] = 1
            
            if store == store_2:
                return True
        
        return False






        