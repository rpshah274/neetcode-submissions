class Solution:
    def encode(self, strs: List[str]) -> str:
        # temp=''
        # for Str in strs:
        #     temp+="-".join(Str)+'.'
        # return temp
        temp=''
        for Str in strs:
            temp+=str(len(Str))+'#'+Str
        return temp
    def decode(self, s: str) -> List[str]:
        # dec=[]
        # word=''
        # for ch in s:
        #     if ch!='-' and ch!='.':
        #         word+=ch
        #     if ch=='.':
        #         dec.append(word)
        #         word=''
        # return dec
        dec=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            dec.append(s[i:j])
            i=j
        return dec
            