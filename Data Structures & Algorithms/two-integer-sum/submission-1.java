class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> store = new HashMap<>(); 

        for(int i = 0; i < nums.length; ++i){
            store.put(nums[i],  i);
        }

        for(int i= 0; i < nums.length; i++){
            int needed = target - nums[i]; 

            if(store.containsKey(needed) && store.get(needed) !=i){

                return new int[]{i, store.get(needed)};
              
            }
        }return new int[0];
    }
}
