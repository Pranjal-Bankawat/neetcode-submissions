class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        
        i = 0
        while i < len(s):
            c = s[i]
            j = i
            while c != '#':
                j = j+1
                c = s[j]
            length = int(s[i:j])
            decoded.append(s[j+1:length + j + 1])
            i = length + j + 1
        return decoded