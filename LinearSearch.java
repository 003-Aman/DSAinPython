public class LinearSearch{
    public static void main(String[] args){
        int arr[]={100,90,80,70,50,69,79,89,99};
        int target = 50;
        int answer = linearSearch(arr, target);
        System.out.println("The number is "+target+" and is in the index "+answer+".");


    }

    static int linearSearch(int[] arr, int target){
        if (arr.length ==0){
            return -1;
        }
        for(int index =0;index <arr.length;index++){
            int element = arr[index];
            if(element == target){
                return index;
            }
        }
        return -1;
    }
    
}