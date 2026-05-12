public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        HashSet<int> s = new HashSet<int>(nums);
        int max_ = 0;

        foreach (int n in s)
        {
            if (!s.Contains(n - 1))
            {
                int length = 1;
                while (s.Contains(n + length))
                {
                    length++;
                }
                max_ = Math.Max(max_, length);
            }
        }
        return max_;
    }
}