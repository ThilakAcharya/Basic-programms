#include <stdio.h>
#include <stdlib.h>

#define STACK_SIZE 10

int push(int item,int *top,int s[])
{
    if(*top == STACK_SIZE - 1){
        printf("stack is full");
        return 0;
    }
    s[++*top] = item; /*incremet the stack pointer and then insert */
    return 0;
}
int pop(int *top,int s[])
{
    int item;
    if(*top == -1)
    {
        printf("\nstack empty");
        return 0;
    }
    item = s[(*top)--];
    return 0;
}
int display(int *top,int s[])
{
    int i;
    if(*top == -1){
        printf("stack is empty");
        return 0;
    }
    printf("contents are: \n");
    for(i=0;i<*top;i++){
        printf("%d\n",s[i]);
    }
}
int main()
{
    int top;
    int s[STACK_SIZE];
    int input,item;
    
    top = -1;
    for(;;){
        printf("\n1.push");
        printf("\n2.pop");
        printf("\n3.display");
        printf("\n4.exit\n");
        scanf("%d",&input);
        switch(input){
            case 1: printf("\n Enter the number to be inseted: ");
                    scanf("%d",&item);
                    push(item,&top,s);
                    break;
            case 2: item=pop(&top,s);
                    if(item != 0);
                        printf("item %d is popped from the stack",item);
                    break;
            case 3: display(&top,s);
                    break;
            case 4: exit(0);
            default: printf("\n incorrect choice");
                    continue;
        }
    }
}
