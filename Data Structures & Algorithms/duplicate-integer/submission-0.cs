public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> n = new HashSet<int>(nums);

        if (n.Count == nums.Length)
        {
            return false;
        }
        else 
        {
            return true;
        }
    }
}