#include <stdio.h>

int main()
{
    int r;
    printf("Enter the number you want to check: ");
    scanf(" %d", &r);

    if (r % 5 == 0)
    {
        printf("Your number %d ",r "is divisible by 5");
    }
    else{

        printf("Your number",r " is not Divisible by 5" );
    }
    return 0;
}