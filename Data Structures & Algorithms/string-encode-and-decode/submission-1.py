class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(str(len(s)) + '#' + s)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        curr_str = ''
        n = 0
        num_str = ''
        for ch in s:
            if ch == '#' and n == 0:
                n = int(num_str)

                if n == 0:
                    decoded_string.append(curr_str)
                      
            elif n > 0:
                curr_str += ch
                n -= 1
                if n == 0:
                    decoded_string.append(curr_str)
                    curr_str = ''
                    num_str = ''
            else:
                num_str += ch
        return decoded_string
                