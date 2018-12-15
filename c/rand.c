#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000

int a[N];

void gen_random(int upper_bound) {
  int i;
  for(i = 0; i < N; i++)
    a[i] = rand() % upper_bound;
}

void print_random() {
  int i;
  for(i = 0; i < N; i++)
    printf("%d ", a[i]);
  printf("\n");
}

int howmany(int value) {
  int count = 0, i;
  for (i = 0; i < N; i ++)
    if (a[i] == value)
      ++count;
  return count;
}

int main(void) {
  srand(time(NULL)); 
  int i, histogram[10] = {};

  gen_random(10);
  for (i = 0; i < 10; i ++)
    // histogram[i] = howmany(i);
    ++histogram[a[i]];
  print_random();
  return 0;

}