public class Solution {
    public int SubarraySum(int[] nums, int k) {
        int res = 0;
        int curSum = 0;
        Dictionary<int,int> prefSum = new Dictionary<int,int>();
        prefSum[0] = 1;

        foreach (int n in nums)
        {
            curSum += n;

            int diff = curSum - k;

            if (prefSum.ContainsKey(diff)) 
            {
                res += prefSum[diff];
            }

            if (!prefSum.ContainsKey(curSum))
            {
                prefSum[curSum] = 0;
            }
            prefSum[curSum]++;
        }
        
        return res;
    }
}