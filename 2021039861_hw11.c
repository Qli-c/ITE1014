#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y;
    int* pi;
    int k=0;

    scanf("%d %d", &x, &y);

    pi = (int*)malloc(x*y*sizeof(int));

    for(int i=0; i<(x*y); i++)
    {
        scanf("%d", &pi[i]);
    }

    printf("%d %d\n",x,y);

    for(int i=0; i<y; i++)
    {
        for(int j=0; j<x; j++)
        {
            printf("%d ", pi[k]);
            k++;
        }
        printf("\n");
    }

    free(pi);
    return 0;
}
