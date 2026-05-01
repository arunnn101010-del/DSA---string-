# Promblem - strinf to interger 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 8 & medium 
class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        int sign = 1;
        int n = s.size();
        long result = 0;

        while(i < n && s[i] == ' ') {
            i++;
        }

        if(i < n && (s[i] == '+' || s[i] == '-')) {
            if(s[i] == '-') sign = -1;
            i++;
        }

        while(i < n && isdigit(s[i])) {
            int digit = s[i] - '0';
            result = result * 10 + digit;

            if(result * sign > INT_MAX) return INT_MAX;
            if(result * sign < INT_MIN) return INT_MIN;
            i++;
        }
        return result*sign;
    }
};
