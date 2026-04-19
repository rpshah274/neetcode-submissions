class Solution:

    def encode(self, strs: List[str]) -> str:
        temp=''
        for Str in strs:
            temp+="-".join(Str)+'.'
        return temp
    def decode(self, s: str) -> List[str]:
        dec=[]
        word=''
        for ch in s:
            if ch!='-' and ch!='.':
                word+=ch
            if ch=='.':
                dec.append(word)
                word=''
        return dec
