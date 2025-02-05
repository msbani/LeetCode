class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long ans = 0, no = 0;
        for(int i:nums) {
            if(i != 0) no = 0;
            else ans += ++no;
        }
        return ans;
    }
}