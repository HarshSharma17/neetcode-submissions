class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        i = 0
        sum = 0

        while(i < len(s)):
            if i < len(s) - 1:
                twostring = s[i: i + 2]
                if twostring in values:
                    sum += values.get(twostring)
                    i += 2
                    continue
            
            onestring = s[i:i+1]
            sum += values.get(onestring)
            i += 1

        return sum