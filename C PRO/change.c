#include<stdio.h>
int main(){
    int dodo, gogo;
    int total,deposit,change,rest,menu;
    int w500,w100,w50,w10;
    int cnt_dodo,cnt_gogo;
    while(1){
        printf("�ǶǸ� 70��, �ǲǹ� 30��\n");
        printf("���� ������ �Է��ϼ���\n");
        scanf("%d %d",&cnt_dodo,&cnt_gogo);
        dodo=70*cnt_dodo;
        gogo=30*cnt_gogo;
        total=dodo+gogo;
        printf("�� �ݾ��� %d�Դϴ�\n",total);
        printf("���� �� �ݾ��� �Է��ϼ���\n");
        scanf("%d",&deposit);
        if (deposit>=total){
            change=deposit-total;
            w500=change/500;
            w100=change%500/100;
            w50=change%100/50;
            w10=change%50/10;
            printf("500��:%d,100��:%d,50��:%d,10��:%d\n",w500,w100,w50,w10);
            printf("����Ϸ��� 1, �ƴϸ�:");
            scanf("%d",&menu);
            if(menu==0)break;
            else continue;
        }
        else{
            printf("�ݾ��� �����մϴ�");
            break;
        }
    }
    return 0;
}