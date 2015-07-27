public class Solution {
    public int[] TwoSum(int[] nums, int target) {
            int [] result = {};

            int [] sorted = new int[nums.Length];
            Array.Copy(nums, sorted, nums.Length);
            
            Array.Sort(sorted);
            int i = 0;
            var j = sorted.Length - 1;
            int diff = 0;

            while (i < j)
            {
                diff = target - sorted[i] - sorted[j];

                if (diff > 0)
                {
                    i++;
                }
                else if (diff < 0)
                {
                    j--;
                }
                else
                {
                    result = new int[2];
                    result[0] = Array.IndexOf(nums, (sorted[i])) + 1;
                    result[1] = Array.LastIndexOf(nums, sorted[j]) + 1;

                    Array.Sort(result);
                    return result;
                }
            }

            return result;     
    }
}