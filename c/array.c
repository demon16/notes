#include <stdio.h>

struct Complex {
  double x, y;
} a[4];

struct {
  double x, y;
  int count[4];
} s;

int main(void) {
  int count[4];
  count[0] = 7;
  int i;
  for(i = 0; i<4; i++) {
    printf("%d\n", count[i]);
    printf("%d\n", ++count[i]);
    printf("%d\n", count[i]);
  }
  return 0;
}
