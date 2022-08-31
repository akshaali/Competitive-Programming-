void bubbleSort(vector<int>& arr, int n)
{   
    // Write your code here.
    int start = 0, end = arr.size()-1;
    while(start < end){
        for(int i = 0; i< end - start; i++){
            if(arr[i]>arr[i+1]){
                swap(arr[i], arr[i+1]);
            }
        }
        start++;
    }
    
}
