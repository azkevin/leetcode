import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numsToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numsToIndex.containsKey(target - nums[i])) {
                return new int[] {numsToIndex.get(target - nums[i]), i};
            }
            numsToIndex.put(nums[i], i);
        }
        throw new IllegalArgumentException();
    }

    // Time complexity: O(n^2)
    // Space complexity: O(n)
    public int[] twoSumBF(int[] nums, int target) {
        int[] indices = {};
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    indices = new int[] {i, j};
                    return indices;
                }
            }
        }
        return indices;
    }
    public static void main (String args[]) {
        TwoSum twoSum = new TwoSum();
        System.out.println(Arrays.toString(twoSum.twoSum(new int[]{2,7,11,15}, 9)));
        System.out.println(Arrays.toString(twoSum.twoSum(new int[]{3,2,4}, 6)));
        System.out.println(Arrays.toString(twoSum.twoSum(new int[]{3,3}, 6)));
    }
}