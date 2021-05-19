#include <stdio.h>

int main()
{
    int n;
    int arr[10010];
    int min;
    int num;
    scanf("%d", &n);

    for(int i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");

    for(int j=0; j<n-1; j++)
    {
        min=arr[j];
        num=j;
        for(int i=j; i<n; i++)
        {
            if(arr[i]<min)
            {
                min=arr[i];
                num=i;
            }
        }
        arr[num]=arr[j];
        arr[j]=min;
    }

    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }

}
