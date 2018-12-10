#include <stdio.h>
#include <math.h>

int factorial(int n){
  int result = 1;
  while (n > 0) {
    result = result * n;
    n = n - 1;
  }
  return n;
}

void test_for(int n){
  for(int i = 1; i < n; i ++){
    printf("%d", i);
  }
}

void print_table(void){
  printf("\n");
  int i, j;
  for(i = 1; i <= 9; i++){
    for(j = 1; j <= i; j++)
      printf("%d\t", i*j);
    printf("\n");
  }
}

int main(void){
  // printf("Hellow, World.\n");
  // char firstletter = 'a';
  // int hour = 11, minute = 59;
  // int total_minute = hour * 60 + minute;
  // printf("firstletter: %c, %d:%d", firstletter, hour, minute);
  // printf("total minute: %d", total_minute);
  // printf("sin(hour): %f", sin(hour));
  int day = 8;
  switch(day){
    case 1:
      printf("Monday\n");
      break;
    case 2:
      printf("Tuesday\n");
      break;
    default:
      printf("Unknown\n");
      break;
  }
  test_for(5);
  print_table();
  
  return 0;
}