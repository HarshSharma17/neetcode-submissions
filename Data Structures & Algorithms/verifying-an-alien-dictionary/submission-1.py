class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderInd = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if orderInd[w1[j]] > orderInd[w2[j]]:
                        return False
                    break
            else:
                # If all characters matched so far,
                # then shorter word should come first
                if len(w1) > len(w2):
                    return False
        
        return True