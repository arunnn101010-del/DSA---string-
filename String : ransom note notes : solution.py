# Promblem - ransome note 
# Appraoch - frequency count 
# Time and space complexity - 0(n+m) & o(n)
# Leetcode and diffculty level - 383 & easy 
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> freq(26,0);

        for(char c : magazine) {
            freq[c - 'a']++;
        }
        for(char c : ransomNote) {
            freq[c - 'a']--;

            if(freq[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};
