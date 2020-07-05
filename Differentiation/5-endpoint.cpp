#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <iomanip>
#include "../true.h"

using namespace std;

double f(double x);

struct Coord { double x, y = 0; };
struct Coords {
   Coord *c;
   Coord operator [] (int i) { return c[i]; }
   const Coord operator [] (int i) const { return c[i]; }

   Coords(const initializer_list<double> &init)
   : c(init.size() ? new Coord[init.size()] : nullptr)
   { for (int i = 0; i < init.size(); i++) *(c + i) = { *(init.begin() + i), f(*(init.begin() + i))}; }

   Coords(const initializer_list<Coord> &init)
   : c(init.size() ? new Coord[init.size()] : nullptr)
   { for (int i = 0; i < init.size(); i++) *(c + i) = *(init.begin() + i); }

};

double f(double x) {
   return
   /* f(x): */ x * exp(x);
   ;
}

double g(double x) {
   return (x + 1) * exp(x);
}

int main() {

   const Coords c = {
      // x values (or {x, y} pairs):
      {1.8, 10.889365}, {1.9, 12.703199}, {2.0, 14.778112},
      {2.1, 17.148957}, {2.2, 19.85503}
   };

   double h =
   /* x to approximate: */ 0.1
   ;
   double x =
   /* x to approximate: */ 1.8
   ;

   cout << "true value: " << g(x) << endl;
   cout << "formula: " << endl;
   cout << "f'(x) = (1/12h) * [-25f(x) + 48(x+h) - 36f(x+2h) + 16f(x+3h) - 3f(x+4h)]" << endl;

   printf("f'(%.6g) = (1/12(%.6g)) * [-25f(%.6g) + 48f(%.6g+%.6g) - 36f(%.6g+2(%.6g)) + 16f(%.6g+3(%.6g)) - 3f(%.6g+4(%.6g))]\n", x, h, x, x, h, x, h, x, h, x, h);

   printf("f'(%.6g) = %.6g * [-25f(%.6g) + 48f(%.6g) - 36f(%.6g) + 16f(%.6g) - 3f(%.6g)]\n", x, (1/(12*h)), x, x + h, x + 2 * h, x + 3 * h, x + 4 * h);

   printf("f'(%.6g) = %.6g * [-25(%.6g) + 48(%.6g) - 36(%.6g) + 16(%.6g) - 3(%.6g)]\n", x, (1/(12*h)), f(x), f(x + h), f(x + 2 * h), f(x + 3 * h), f(x + 4 * h));

   printf("f'(%.6g) = %.6g", x, (1/(12 * h)) * ((-25 * f(x)) + (48 * f(x + h)) - (36 * f(x + 2 * h)) +  (16 * f(x + 3* h)) - (3 * f(x + 4 * h))));

   return 0;
}