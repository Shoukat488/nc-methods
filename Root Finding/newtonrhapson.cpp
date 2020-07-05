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
   /* f(x): */ (pow(x,3) * 2) - 11.7 * pow(x, 2) + 17.7*x - 5
   ;
}

// derivative
double g(double x) {
   return 
   /* f'(x): */ 6*pow(x, 2)-23.4*x + 17.7
   ;
}

int main() {

   int it = 
   /* iterations: */ 10
   ;
   double ea, a, x= 
   /* initial: */ 3
   ;
   double t = findRoot(f, x + 100, x - 100);

   cout << fixed << showpoint << setprecision(6);
   cout << "true value: " << t << endl;
   cout << "\ni\tXi\t\tf(Xi)\t\tf'(Xi)\t\tXi+1\t\tEa(%)\t\tEt(%)" << endl;

   for (int i = 0; i < it; ++i) {
      ea = x;
      a = x - (f(x) / g(x));
      ea = ((a - ea) / a);
      cout  << i + 1 << "\t"
            << x << "\t"
            << f(x) << "\t"
            << g(x) << "\t"
            << a << "\t"
            << abs(i ? ea * 100 : 0) << "\t"
            << abs((t - a) / t) * 100
            << endl;
      x = a;
   }

   return 0;
}



