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
   /* x to approximate: */ 2.0
   ;

   cout << "true value: " << g(x) << endl;  
   cout << "formula: " << endl;
   cout << "f'(x) = (1/2h) * [-3f(x) + 4f(x+h) - f(x+2h)]" << endl;

   printf("f'(%.6g) = (1/2(%.6g)) * [-3f(%.6g) + 4f(%.6g + %.6g) - f(%.6g+2(%.6g))]\n", x, h, x, x, h, x, h);

   printf("f'(%.6g) = %.6g * [-3f(%.6g) + 4f(%.6g) - f(%.6g)]\n", x, (1/(2*h)), x, x + h, x + 2*h);

   printf("f'(%.6g) = %.6g * [-3(%.6g) + 4(%.6g) - %.6g]\n", x, (1/(2*h)), f(x), f(x + h), f(x + 2*h));

   printf("f'(%.6g) = %.6g", x, (1/(2 * h)) * (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)));

   return 0;
}