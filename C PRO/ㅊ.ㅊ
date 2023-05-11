#include<stdio.h>
int main(){
    int dodo, gogo;
    int total,deposit,change,rest,menu;
    int w500,w100,w50,w10;
    int cnt_dodo,cnt_gogo;
    while(1){
        printf("또또면 70원, 꽁꽁바 30원\n");
        printf("각각 개수를 입력하세요\n");
        scanf("%d %d",&cnt_dodo,&cnt_gogo);
        dodo=70*cnt_dodo;
        gogo=30*cnt_gogo;
        total=dodo+gogo;
        printf("총 금액은 %d입니다\n",total);
        printf("투입 할 금액을 입력하세요\n");
        scanf("%d",&deposit);
        if (deposit>=total){
            change=deposit-total;
            w500=change/500;
            w100=change%500/100;
            w50=change%100/50;
            w10=change%50/10;
            printf("500원:%d,100원:%d,50원:%d,10원:%d\n",w500,w100,w50,w10);
            printf("계속하려면 1, 아니면:");
            scanf("%d",&menu);
            if(menu==0)break;
            else continue;
        }
        else{
            printf("금액이 부족합니다");
            break;
        }
    }
    return 0;
}