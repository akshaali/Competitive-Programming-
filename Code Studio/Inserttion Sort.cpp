void insertionSort(int n, vector<int> &arr){
    // Write your code here.
    int start = 1, end = arr.size();
    while(start<end){
        int temp = arr[start];
        int j = start-1;
        for(;j>=0;j--){
            if(arr[j]>temp){
                arr[j+1] = arr[j];
            }else{
                break;
            }
        }
        arr[j+1] = temp;
        start++;
    }
    
}
