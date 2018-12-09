#include <stdio.h>
#include <math.h>

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
  
  return 0;
}