
#include<stdio.h>
#include<stdlib.h>

int main(){
    int num;
    FILE *fptr;

    fptr = fopen("index.txt", "w");
    if(fptr == NULL){
        printf("ERROR!!!");
        exit(1);
    }
    printf("Enter Num: ");
    scanf("%d", &num);

    fprintf(fptr, "Number is: %d", num);
    fclose(fptr);
    return 0;

}
