#include <math.h>
#include <functional>
#define _USE_MATH_DEFINES

using namespace std;


double findRoot(function<double (double)> f, double a = -100, double b = 100, double it = 100) {
   double x, y;
   for (int i = 0; i < it; ++i) {
      x = (a + b) / 2;
      if (f(x) > 0 && f(a) > 0) a = x;
      else if (f(x) < 0 && f(a) < 0) a = x;
      else b = x;
      if (x == y) return x;
      y = x;
   } return x;
}