#include <stdio.h>

int main()
{
    int arr[10010];
    int n;
    int answer;
    scanf("%d",&n);
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    answer = arr[0];

    for(int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);

        if(answer < arr[i])
        {
            answer = arr[i];
        }
    }
    printf("\n");
    printf("%d\n",answer);
    return 0;
}
