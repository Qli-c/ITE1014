#include <stdio.h>

int main()
{
    int a,b,c = 0;
    int r = 0;

    scanf("%d %d",&a,&b);

    if(a<b)
    {
        c = b;
        b = a;
        a = c;
    }
    r = a%b;

    while (r != 0)
    {
        a = b;
        b = r;
        r = a%b;
    }
    printf("%d\n",b);

    return 0;
}
