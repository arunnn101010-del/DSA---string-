# Promblem - generate parentheses 
# Approach - backtracking 
# Time and space complexity - 0(n^2) & 0(1)
# leetcode & diffculty level - 22 & medium
class Solution {
public:
    void solve(int open, int close, int n, string curr, vector<string>& res) {

        if(curr.size() == 2 * n) {
        res.push_back(curr);
        return;
        }

        if(open < n) {
        solve(open+1, close, n, curr + '(', res);
        }

        if(close < open) {
        solve(open, close+1, n, curr + ')', res);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        solve(0, 0, n, "", res);
        return res;
    }
};
