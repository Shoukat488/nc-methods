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
#include "../true.h"

using namespace std;

double f(double x) {
   return 
   /* f(x): */ sin(pow(x, 2))
   ;
}


int main() {

   int it = 
   /* iterations: */ 20
   ;
   double a, ea, x0 = 
   /* x0: */ -1
   ;
   double x1 = 
   /* x1: */ -2
   ;
   double t = findRoot(f, x0, x1);

   cout << fixed << showpoint << setprecision(6);
   cout << "true value: " << t << endl;
   if (f(x0) * f(x1) > 0) {
      cout << "Invalid inputs" << endl;
      return 0;
   }
   cout << "\ni\tXi-1\t\tXi\t\tf(Xi-1)\t\tf(Xi)\t\tXi+1\t\tEa(%)\t\tEt(%)" << endl;
   
   for (int i = 0; i < it; ++i) {
      ea = a;
      a = x1 - (f(x1) / ((f(x1) - f(x0)) / (x1 - x0)));
      ea = ((a - ea) / a);
      cout  << i + 2 << "\t"
            << x0 << "\t"
            << x1 << "\t"
            << f(x0) << "\t"
            << f(x1) << "\t"
            << a << "\t"
            << abs(i ? ea * 100 : 0) << "\t"
            << abs((t - a) / t) * 100
            << endl;
      x0 = x1;
      x1 = a;
   }

   return 0;
}



