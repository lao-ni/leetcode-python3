class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            if 'R' in board[i]:
                hang=i
                break
        for j in range(len(board[i])):
            if board[i][j]=='R':
                lie=j
                break
        #print(hang,lie)
        count=0
        s=''.join(board[hang])
        s=s.replace('.','')
        #print(s)
        if 'Rp' in  s:
            count+=1
        if 'pR' in s:
            count+=1
        s=''.join(board[i][lie] for i in range(8))
        s=s.replace('.','')
        #print(s)
        if 'Rp' in  s:
            count+=1
        if 'pR' in s:
            count+=1
        return count
        
