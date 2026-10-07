class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = 0
        right_rem = 0
        
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        ans = set()

        def dfs(i, l_rem, r_rem, open_cnt, path):
            if i == len(s):
                if l_rem == 0 and r_rem == 0 and open_cnt == 0:
                    ans.add(path)
                return
            
            if l_rem < 0 or r_rem < 0 or open_cnt < 0:
                return

            char = s[i]

            if char == '(':
                dfs(i + 1, l_rem - 1, r_rem, open_cnt, path)
                dfs(i + 1, l_rem, r_rem, open_cnt + 1, path + '(')
            elif char == ')':
                dfs(i + 1, l_rem, r_rem - 1, open_cnt, path)
                dfs(i + 1, l_rem, r_rem, open_cnt - 1, path + ')')
            else:
                dfs(i + 1, l_rem, r_rem, open_cnt, path + char)

        dfs(0, left_rem, right_rem, 0, "")
        return list(ans)