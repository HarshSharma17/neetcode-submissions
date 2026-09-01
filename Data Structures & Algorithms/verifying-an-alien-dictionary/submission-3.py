class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = dict()

        for index,value in enumerate(order):
            ordermap[order[index]] = index

        for i in range(len(words)-1):
            for j in range(len(words[i])):

                if j >= len(words[i+1]):
                    return False

                if words[i][j] != words[i+1][j]:
                    currletter = ordermap[words[i][j]]
                    nextletter = ordermap[words[i+1][j]]

                    if nextletter < currletter:
                        return False
                    else:
                        break
        return True
