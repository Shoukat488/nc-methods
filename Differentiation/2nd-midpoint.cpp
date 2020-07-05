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

double i(double x) {
   return (x + 1) * exp(x) + exp(x);
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
   /* x to approximate: */ 2.0
   ;

   cout << "true value: " << i(x) << endl;
   cout << "formula: " << endl;
   cout << "f''(x) = (1/h^2) * [f(x-h) - 2f(x) + f(x + h)]" << endl;

   printf("f''(%.6g) = (1/(%.6g)^2) * [f(%.6g-%.6g) - 2f(%.6g) + f(%.6g+%.6g)]\n", x, h, x, h, x, x, h);

   printf("f''(%.6g) = %.6g * [f(%.6g) - 2f(%.6g) + f(%.6g)]\n", x, (1/(h * h)), x - h, x, x + h);

   printf("f''(%.6g) = %.6g * [%.6g - 2(%.6g) + %.6g]\n", x, (1/(h * h)), f(x - h), f(x), f(x + h));

   printf("f''(%.6g) = %.6g", x, (1/(h * h)) * (f(x - h) - (2 * f(x)) + f(x + h)));

   return 0;
}