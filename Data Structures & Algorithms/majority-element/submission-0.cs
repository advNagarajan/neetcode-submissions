public class Solution {
    public int MajorityElement(int[] nums) {
        int elem = nums[0];
        int count = 1;

        foreach (int n in nums[1..]) 
        {
            if (elem == n)
            {
                count++;
            }
            else 
            {
                count--;
            }
            if (count < 0)
            {
                elem = n;
                count = 1;
            }
        }

        return elem;
    }
}