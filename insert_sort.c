#include<stdio.h>
#define MaxSize 6
typedef int data;
int main(){
    data R[MaxSize]={0,5,-3,4,2,6};
    int i,j;
    for(i=2;i<MaxSize;i++){
        R[0]=R[i]; //�����i�������ü�����
        //���ֲ��ң�
		int low = 1, high = i-1;
		while(low<=high){
			int m = (low+high)/2;
			if(R[0]<R[m]){
				high = m-1; //������ڵͰ��� 
			}else low = m+1;
		} 
        for(j=i-1;j>=high+1;j--){
            R[j+1]=R[j]; //��¼����
        }
        R[j+1]=R[0]; //���� 
    }
    for(i=1;i<MaxSize;i++){
    	printf("%d ",R[i]);
	}
    return 0;
}
