public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> s = new Dictionary<int,int>();

        for (int i = 0; i < nums.Length; i++)
        {
            s[nums[i]] = i;
        }

        for (int i = 0; i < nums.Length; i++)
        {
            int temp = target - nums[i];

            if (s.ContainsKey(temp) && i != s[temp])
            {
                return new int[] { i, s[temp] };
            }
        }

        return new int[] { };
    }
}
