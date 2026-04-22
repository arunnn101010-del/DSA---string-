# Promblem - Valid anagram 
# Approach - Hashing
# Time and space complexity - O(n) & O(1)
# Leetcode and diffculty level - 242 & easy
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        vector<int> freq(26,0);

        for(int i=0; i<s.size(); i++) {
            freq[s[i] - 'a'] ++;
            freq[t[i] - 'a'] --;
        }

        for(int i=0; i<25; i++) {
            if(freq[i] != 0) return false;
        }
        return true;
    }
};
