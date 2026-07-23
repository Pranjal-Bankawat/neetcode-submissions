class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(str(len(s)) + '#' + s)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the delimiter "#"
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract length of the string
            length = int(s[i:j])

            # Extract the actual string
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)

            # Move pointer forward
            i = j + 1 + length
        
        return decoded
                