public class Solution {
    public List<int> MajorityElement(int[] nums) {
        Dictionary<int, int> count = new Dictionary<int, int>();

        foreach (int n in nums)
        {
            if (count.ContainsKey(n))
                count[n]++;
            else
                count[n] = 1;

            if (count.Count <= 2)
                continue;

            Dictionary<int, int> newCount = new Dictionary<int, int>();

            foreach (var kvp in count)
            {
                int num = kvp.Key;
                int c = kvp.Value;

                if (c > 1)
                    newCount[num] = c - 1;
            }

            count = newCount;
        }

        List<int> res = new List<int>();

        foreach (int n in count.Keys)
        {
            if (nums.Count(x => x == n) > nums.Length / 3)
                res.Add(n);
        }

        return res;
    }
}