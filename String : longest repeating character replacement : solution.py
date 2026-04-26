# Promblem - longest repeating character replacement 
# Approach - sliding window + frequency count
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 424 & medium 
class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> freq(26,0);
        int l = 0, maxFreq = 0, ans = 0;

        for(int r=0; r<s.size(); r++) {
            freq[s[r] - 'A']++;

            maxFreq = max(maxFreq, freq[s[r] - 'A']);

            while((r - l + 1) - maxFreq > k) {
                freq[s[l] - 'A']--;
                l++;
            }
            ans = max(ans, r-l+1);
        } 
        return ans;
    }
};
