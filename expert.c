#include <stdio.h>
#include <stdlib.h>  //declaration of "atoi" function

int sum_mult(int, int);

int main(int argc, char *argv[])
{
  int a;
  if(argc!=2){
    printf("please use \"prg_name value\"\n");
    return -1;
  }	
  a = atoi(argv[1]);      	       
  printf("Answer is: %d\n",sum_mult(a,3)+sum_mult(a,5)-sum_mult(a,15));
  return 0;
}

int sum_mult(int tar, int n)
{
  int n_max = (tar%n==0)?(tar/n-1):(tar/n);
  return (n_max+1)*(n_max)*n/2; 
}
