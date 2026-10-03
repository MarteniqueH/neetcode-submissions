class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0; 
        }

        int left = 0;
        int right = height.length - 1; 

        int leftTallest = height[left]; 
        int rightTallest = height[right]; 


        int result = 0;

        while(left < right){
            if(height[left] < height[right]){
                left++;

                leftTallest = Math.max(height[left], leftTallest); 

                result += leftTallest - height[left]; 
            }else{
                right--;

                rightTallest = Math.max(height[right], rightTallest); 

                result += rightTallest - height[right];
            }
        }
        return result;
        
    }
}
