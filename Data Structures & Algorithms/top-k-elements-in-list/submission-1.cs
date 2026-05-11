public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int,int> count = new Dictionary<int,int>();
        foreach (int n in nums) 
        {
            count[n] = count.GetValueOrDefault(n,0) + 1;
        }

        List<int>[] freq = new List<int>[nums.Length + 1];

        for (int i = 0; i < freq.Length; i++)
        {
            freq[i] = new List<int>();
        }

        foreach (var pair in count)
        {
            int c = pair.Key;
            int n = pair.Value;

            freq[n].Add(c);
        }

        List<int> res = new List<int>();

        for (int i = freq.Length - 1; i > 0; i--)
        {
            foreach (int n in freq[i])
            {
                res.Add(n);

                if (res.Count == k)
                {
                    return res.ToArray();
                }
            }
        }

        return res.ToArray();
    }
}
