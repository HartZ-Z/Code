#include <stdio.h>
void main ()
{
    FILE *f1,*f2,*f3;
    int c;

    printf("\n Enter 30 numbers");
    f1=fopen("data",'w');
    for ( int i = 1; i <= 30; i++)
    {
        scanf("%d",&c);
        putw(c,f1);
    }
    fclose(f1);

    f1=fopen("data","r");
    f2=fopen("Odd","w");
    f3=fopen("Even","w");

    for (int i = 1; i <= 30 ; i++)
    {
        c=getw(f1);
        if (c % 2 == 0)
        {
            putw(c,f2);
        }

        else
        {
            putw(c,f3);
        }
    }
    fclose(f1);
    fclose(f2);
    fclose(f3);

    printf("\nOdd data");
    f2=fopen("Odd",'r');

    while ( c=getw(f2)!=EOF )
    {
        printf("%d",c);
    }
    fclose(f2);

    printf("\nEven Data ");
    f3=fopen("Even","r");
    while(c=getw(f3)!=EOF)
    {
        printf("%d",c);
    }
    f3=fclose(f3);
}
