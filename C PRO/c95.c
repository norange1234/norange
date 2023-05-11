#include<stdio.h>
int main(){
    int KOR,ENG,MATH;
    printf("korean:"),scanf("%d",&KOR);
    printf("english:"),scanf("%d",&ENG);
    printf("math:"),scanf("%d",&MATH);
    KOR>=70 && ENG>=70 ||MATH>=80 ? printf("great"):printf("ok");
    return 0;
} 