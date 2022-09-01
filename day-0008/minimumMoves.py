class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        q=deque([([0,1],0,0)])
        def inb(p):return p[0]>=0 and p[0]<len(grid) and p[1]>=0 and p[1]<len(grid[0]) and grid[p[0]][p[1]]==0
        u=set()
        while q:
            p,v,c=q.popleft()
            if p[0]==len(grid)-1 and p[1]==len(grid[0])-1 and v==0:return c
            k=(p[0],p[1],v)
            if k in u:continue
            u.add(k)
            if v==0:
                pn=[p[0],p[1]+1]
                if inb(pn):q.append((pn,v,c+1))
                pn=[p[0]+1,p[1]]
                if inb(pn) and inb([p[0]+1,p[1]-1]):q.append((pn,v,c+1))
                pn=[p[0]+1,p[1]-1]
                if inb(pn) and inb([p[0]+1,p[1]]):q.append((pn,1,c+1))
            elif v==1:
                pn=[p[0]+1,p[1]]
                if inb(pn) and grid[pn[0]][pn[1]]!=1:q.append((pn,v,c+1))
                pn=[p[0],p[1]+1]
                if inb(pn) and inb([p[0]-1,p[1]+1]):q.append((pn,v,c+1))
                pn=[p[0]-1,p[1]+1]
                if inb(pn) and inb([p[0],p[1]+1]):q.append((pn,0,c+1))
        return -1
