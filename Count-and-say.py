class Solution:
    def countAndSay(self, n: int) -> str:
        c=[1]
        for i in range(n-1):
            next=[]
            for t in c:
                if not next or next[-1]!=t:
                    next.append(1)
                    next.append(t)
                else:
                    next[-2]+=1
            c=next
            
        return "".join(map(str,c))
                
