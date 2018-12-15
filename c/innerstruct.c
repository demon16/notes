# include <stdio.h>

enum coordinate_type { RECTANGULAR = 1, POLAR };

struct complex_struct {
  enum coordinate_type t;
  double x, y;
};

struct Segment {
  struct complex_struct start;
  struct complex_struct end;
};

int main(void) {
  printf("%d %d\n", RECTANGULAR, POLAR);
  struct Segment s = {{RECTANGULAR, 1.0, 2.0}, {POLAR, 4.0, 6.0}};
  printf("%d", s.start.t);
  return 0;
}