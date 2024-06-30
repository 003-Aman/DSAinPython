public class QLinearSearch {
    public static void main(String[] args){

        String name = "Aman Shrestha";
        char target = 'h';
        System.out.println(search(name, target));
        int[] arr ={32,45,1,9,87,2};
        int target1 = 9;
        System.out.println(linearSearch(arr, target1, 2, 5));
        System.out.println(min(arr));
        int arr1[][]={{1,2,3,4},{10,20,30,40},{11,21,31,41},{12,22,32,42}};

    }
//Q1.SEARCH A CHARACTER IN A STRING
    static boolean search(String str, char target){
        if(str.length() ==0){
            return false;
        }

        for(int i=0;i<str.length();i++){
            if(target==str.charAt(i)){
                return true;
            }
        }
        return false;
    }

    //Q2.SEARCH FOR A NUMBER IN RANGE
    static int linearSearch(int[] arr, int target,int start, int end){
        if (arr.length ==0){
            return -1;
        }
        for(int index =start;index <end;index++){
            int element = arr[index];
            if(element == target){
                return index;
            }
        }
        return -1;
    }

    //Q3.FIND MINIMUM NUMBER IN THE ARRAY WITHOUT SORTING OFC
    static int min(int arr){
        int ans = arr[0];
        for (int i=1;i<arr.length;i++){
            if(arr[i]<ans){
                ans = arr[i];
            }
        }
        return ans;
    }
    //Q4.SEARCH IN 2D ARRAY
    static int search2D(int[][] arr,int target){}

    
}
