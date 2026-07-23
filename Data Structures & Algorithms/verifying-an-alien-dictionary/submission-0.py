class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderInd = {}

        for i,s in enumerate(order):
            orderInd[s] = i

        for i in range(len(words) - 1):
            w1,w2 = words[i],words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w2[j] != w1[j]:
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False

                    break
        
        return True

        
