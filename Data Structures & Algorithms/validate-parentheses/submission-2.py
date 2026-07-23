class Solution:
    def isValid(self, s: str) -> bool:

        d = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        arr = []

        for bracket in s:
            if bracket in d.keys():
                arr.append(bracket)
            else:
                if len(arr) > 0:
                    last_open_bracket = arr.pop()
                    if d[last_open_bracket] == bracket:
                        continue
                    else:
                        return False
                else:
                    return False

        return len(arr) == 0