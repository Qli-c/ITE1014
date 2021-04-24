#include <stdio.h>

int main()
{
	int num;
	printf("단수를 입력하시오 :\n");
	scanf("%d",&num);
	if(num >= 1 && num <= 9)
	{
		printf("**********%d단**********\n",num);
		for(int i=1;i<10;i++)
		{
			printf("%d*%d= %d\n",num,i,num*i);
		}
		printf("***********************\n");
	}
	else
	{
		printf("잘못된 입력 범위입니다.\n");
	}
	return 0;
}

