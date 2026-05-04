# Promblem - Letter combinations of a phone number
# Appraoch - backtracking 
# Time and space complexity - 0(4^n) & 0(n)
# Leetcode and diffculty level - 17 & medium
class Solution {
public:
    vector<string> res;

    void solve(string &digits, int i,  string curr, vector<string> &map) {

        if(i == digits.size()) {
            res.push_back(curr);
            return;
        }

        string letters = map[digits[i] - '0'];

        for(char c : letters) {
            solve(digits, i+1, curr+c, map);
        }
    }

    vector<string> letterCombinations(string digits) { 
        if(digits == "") return {};

        vector<string> map = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"
        };

        solve(digits, 0, "", map);
        return res;
        
    }
};
