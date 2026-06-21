class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for word in strs:
            
            encoded_string += str(len(word)) +"#"+ word
        
        return encoded_string
    # 5#Hello5#World"
    def decode(self, s: str) -> List[str]:

        i = 0
        output = []
        encoded_string=""
        while i < len(s):
            j = i

            while s[j] != "#":

                j+=1
            
            length_word = int(s[i:j])

            last_index = j+1+length_word
            output.append(s[j+1: last_index])
            i = last_index
        
        return output




