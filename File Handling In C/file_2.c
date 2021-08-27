#include<stdio.h>
#include<stdlib.h>

int main(){
    int num;
    FILE *fptr;

    if((fptr= fopen("index.txt", "r")) == NULL){
        printf("ERRORRR! Opening File...");
        exit(1);
    }

    fscanf(fptr, "%d", &num);
    
    printf("Value of n=%d", num);
    fclose(fptr);
    return 0;
}
