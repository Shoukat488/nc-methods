/*Solution(Root) of equations in one variable: ( 10 %)

bisection
false position
newton rhapson
secant
fixed point

Interpolation and Polynomial approximation: ( 10-15 %)

Lagrange Polynomial
Newton divided, forward, backward, and centered difference
*/
#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <iomanip>
#include "true.h"

using namespace std;

double f(double x) {
   return 
   /* f(x): */ pow(x, 10) - 1
   ;
}

int main() {

   int it = 
   /* iterations: */ 10
   ;
   double x, ea, a = 
   /* a: */ 0
   ;
   double b = 
   /* b: */ 1.3
   ;
   double t = findRoot(f, 0, 1.3);
   
   cout << fixed << showpoint << setprecision(6);
   cout << "\ni\ta\t\tb\t\tx\t\tf(a)\t\tf(b)\t\tf(x)\t\tEa(%)\t\tEt(%)" << endl;
   for (int i = 0; i < it; ++i) {
      ea = x;
      x = (a * f(b) - b * f(a)) / (f(b) - f(a));
      ea = ((x - ea) / x);
      cout  << i + 1 << "\t"
            << a << "\t"
            << b << "\t"
            << x << "\t"
            << f(a) << "\t"
            << f(b) << "\t"
            << f(x) << "\t"
            << (i ? ea * 100 : 0) << "\t"
            << ((t - x) / t) * 100
            << endl;

      if (f(x) > 0 && f(a) > 0) a = x;
      else if (f(x) < 0 && f(a) < 0) a = x;
      else b = x;
   }
   

   return 0;
}



