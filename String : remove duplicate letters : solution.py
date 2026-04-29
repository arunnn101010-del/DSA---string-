# Promblem - Remove duplicate letters 
# Appraoch - stack + greedy 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 316 & medium 
class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> freq(26, 0);
        vector<bool> used(26, false);

        // count frequency
        for(char c : s) {
            freq[c - 'a']++;
        }

        string st = "";

        for(char c : s) {
            freq[c - 'a']--;

            if(used[c - 'a']) continue;

            while(!st.empty() && st.back() > c && freq[st.back() - 'a'] > 0) {
                used[st.back() - 'a'] = false;
                st.pop_back();
            }

            st.push_back(c);
            used[c - 'a'] = true;
        }

        return st;
    }
};
