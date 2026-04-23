# Promblem - reverse string 
# Approach - two pointers 
# Time and space complexity - O(n) & O(1)
# Leetcode and diffculty level - 344 & easy 
class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size()-1;

        while(l < r) {
            swap(s[l], s[r]);
            l++;
            r--;
        }
    }
};
