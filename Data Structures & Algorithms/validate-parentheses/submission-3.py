class Solution:
    def isValid(self, s: str) -> bool:

        d = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        arr = []

        for bracket in s:
            if bracket in d.values():
                arr.append(bracket)
            else:
                if len(arr) > 0:
                    last_open_bracket = arr.pop()
                    if d[bracket] != last_open_bracket:
                        return False
                else:
                    return False
        return len(arr) == 0