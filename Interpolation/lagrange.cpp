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

   Coords(const initializer_list<double> &init)
   : c(init.size() ? new Coord[init.size()] : nullptr)
   { for (int i = 0; i < init.size(); i++) *(c + i) = { *(init.begin() + i), f(*(init.begin() + i))}; }

   Coords(const initializer_list<Coord> &init)
   : c(init.size() ? new Coord[init.size()] : nullptr)
   { for (int i = 0; i < init.size(); i++) *(c + i) = *(init.begin() + i); }

};


double f(double x) {
   return 
   /* f(x): */ log(x);
   ;
}

int main() {

   int n = 
   /* order: */ 3
   ;

   Coords c = {
      // x values (or {x, y} pairs): 
      1, 4, 6
   };

   double x = 2;

   cout << fixed << showpoint << setprecision(6);
   cout << "true value: " << f(x) << endl;

   double result = 0, denom = 0;

   for (int i = 0 ; i < n; i++) {
      for (int j = 0; j < n; j++)
         if (j != i)
            printf("(x-%.6g)", c[j].x);
      cout << c[i].y << "\t";
   } cout << endl;

   for (int i = 0 ; i < n; i++) {
      for (int j = 0; j < n; j++)
         if (j != i)
            printf("(%.6g-%.6g)", c[i].x, c[j].x);
      cout << "\t\t";
   } cout << endl << endl;


   for (int i = 0 ; i < n; i++) {
      double term = c[i].y;
      denom = 1;
      if (c[i].y) {
         for (int j = 0; j < n; j++)
            if (j != i) {
               term *= (x - c[j].x) / double (c[i].x - c[j].x);
               denom *= (c[i].x - c[j].x);
               printf("(x-%.6g)", c[j].x);
            }
         cout << c[i].y / denom << "\t";
      } 
      result += term;
   } cout << endl << endl;

   cout << "lagrange approximation of order " << n << ": " << result;

   return 0;
}