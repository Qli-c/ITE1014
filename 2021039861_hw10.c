#include <stdio.h>

int main()
{
    int n;
    int arr[105];
    int ans[105];
    int min;
    int num;
    int count=0;
    int check;

    scanf("%d", &n);

    for(int i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
        ans[i]=0;
    }


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
        check=0;
        for(int j=0; j<n; j++)
        {
            if(arr[i]==ans[j])
            {
                check=1;
            }
        }
        if (check==0)
        {
            ans[count]=arr[i];
            count++;
        }
    }

    for(int i=0; i<count; i++)
    {
        printf("%d ",ans[i]);
    }

}
