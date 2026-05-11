class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        if len(strs) == 0:
            return output
        
        count_list = [str(len(s)) for s in strs]

        output = output + ",".join(count_list) + "#"
        for s in strs:
            output = output + s
        return output    

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 0:
            return []
        output = []
        tmp = s.split("#", 1)
        count_list = tmp[0].split(",")
        word_str = tmp[1]
        start_index = 0
        for count in count_list:
            end_index = start_index + int(count)
            output.append(word_str[start_index: end_index])
            start_index = end_index
        return output    
            


