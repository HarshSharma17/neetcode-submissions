class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        
        for s in strs:
            # length + '#' + string
            encoded.append(str(len(s)) + '#' + s)
        
        return ''.join(encoded)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the separator to get the length
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length
            length = int(s[i:j])
            
            # Move to start of actual string
            j += 1
            
            # Extract string using known length
            word = s[j:j+length]
            res.append(word)
            
            # Move pointer to next encoded word
            i = j + length
        
        return res
