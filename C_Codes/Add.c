#include <stdio.h>
#include <conio.h>
void main()
{
    int a[5] = {1, 2, 3, 4, 5};
    int i = 0;
    clrscr();
    for (i = 0; i < 5; i++);
    {
        printf("%d ", a[i]);
    }
    getch();
}