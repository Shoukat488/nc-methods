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

void r1(const Coords &c, int start, int end) {
   if (start == end) cout << "f(x0) + ";
   else {
      r1(c, start, end - 1);
      for (int i = start; i < end; i++)
         printf("(x-x%d)", i);
      cout << "f[";
      for (int i = end; i >= start; i--)
         printf("x%d, ", i);
      cout << "\b\b] + ";
   }
}

void r2(const Coords &c, int start, int end) {
   if (start == end) printf("f(%.6g) + ", c[start].x);
   else {
      r2(c, start, end - 1);
      for (int i = start; i < end; i++)
         printf("(x-%.6g)", c[i].x);
      cout << "f[";
      for (int i = end; i >= start; i--)
         printf("%.6g, ", c[i].x);
      cout << "\b\b] + ";
   }
}

double solveNoPrint(Coords c, int start, int end) {
   return end - start == 1
      ? (c[end].y - c[start].y) / (c[end].x - c[start].x)
      : (solveNoPrint(c, start + 1, end) - solveNoPrint(c, start, end - 1)) / (c[end].x - c[start].x);
}
void r3(const Coords &c, int start, int end) {
   if (start == end) printf("%.6g + ", c[start].y);
   else {
      r3(c, start, end - 1);
      for (int i = start; i < end; i++)
         printf("(x-%.6g)", c[i].x);
      printf("%.6g + ", solveNoPrint(c, start, end));
   }
}

double prod(const Coords &c, int start, int end, double x) {
   double p = 1;
   for (int i = start; i < end; i++)
      p *= (x - c[i].x);
   return p;
}

double r4(const Coords &c, int start, int end, double x) {
   return start == end
   ? c[start].y
   : prod(c, start, end, x) * solveNoPrint(c, start, end) + r4(c, start, end - 1, x);
}

double solve(Coords c, int start, int end) {
   if (end - start == 1) {
      double ret = (c[end].y - c[start].y) / (c[end].x - c[start].x);
      printf("solving f[%.6g, %.6g]\nf(%.6g) - f(%.6g) = %.6g\n(%.6g - %.6g)\n", c[end].x, c[start].x,
      c[end].x, c[start].x, ret, c[end].x, c[start].x);
      return ret;
   }
   else {
      double right = solve(c, start, end - 1);
      double left = solve(c, start + 1, end);

      double ret = (left - right) / (c[end].x - c[start].x);

      cout << "solving f[";
      for (int i = end; i >= start; i--)
         printf("%.6g, ", c[i].x);
      cout << "\b\b]\n";

      cout << "f[";
      for (int i = end; i >= start + 1; i--)
         printf("%.6g, ", c[i].x);

      cout << "\b\b] - f[";
      for (int i = end - 1; i >= start; i--)
         printf("%.6g, ", c[i].x);

      printf("\b\b] = %.6g\n", ret);
      printf("(%.6g - %.6g)\n", c[end].x, c[start].x);

      return ret;
   }
}

double f(double x) {
   return
   /* f(x): */ log(x + 1)
   ;
}

int main() {

   int n =
   /* terms: */ 4
   ;

   const Coords c = {
      // x values (or {x, y} pairs):
      {30,148},{35,96},{45,68},{55,34}
   };

   double x =
   /* x to approximate: */ 40
   ;

   cout << fixed << showpoint << setprecision(6);
   // cout << "true value: " << f(x) << endl;

   cout << "formula: " << endl;
   r1(c, 0, n - 1);
   cout << endl << endl;

   solve(c, 0, n - 1);

   cout << endl << "formula with values: " << endl;
   r2(c, 0, n - 1);
   cout << "\n= ";
   r3(c, 0, n - 1);

   printf("\nvalue at f(%.6g) = %.6g", x, r4(c, 0, n - 1, x));
   return 0;
}