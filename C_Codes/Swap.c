#include<stdio.h>
int swap (int a , int b);
int main()
{
    int a,b,c;
    printf("enter your two numbers ");
    scanf("%d %d", &a,&b);
    swap(a,b);
    printf("%d %d",a,b);
    return 0;
}

int swap(int a , int b)
{
    int c;
    c=a;
    a=b;
    b=c;
}
