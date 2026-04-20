# Promblem - Valid palindrome
# Appraoch - two pointers 
# Time and space complexity - O(n) & O(1)
# Leetcode and diffcu;ty level - 125 & easy 
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;

        while(l < r) {
            if(!isalnum(s[l])) {
                l++;
            }
            else if(!isalnum(s[r])) {
                r--;
            }
            else {
                if(tolower(s[l]) != tolower(s[r])) {
                    return false;
                }
                l++, r--;
            }
        }
        return true;
    }
};
