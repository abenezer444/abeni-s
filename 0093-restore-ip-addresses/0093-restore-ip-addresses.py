class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        output = []
        
        def valid(start, end):
            if int(s[start:end]) <= 255:
                if len(s[start:end]) > 1 and s[start] != "0" or len(s[start:end]) == 1:
                    return True
            return False
            
        def backtrack(cur, start):
            if len(cur) == 4:
                if start >= len(s):
                    output.append(".".join(cur))
                return

            for idx in range(start, len(s)):
                if valid(start, idx+1):
                    cur.append(s[start:idx+1])
                    backtrack(cur, idx+1)
                    cur.pop()
                else:
                    return 
            return 
    
        for idx in range(3):
            if valid(0, idx+1):
                backtrack([s[:idx+1]], idx + 1)
        return output