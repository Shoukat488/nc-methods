#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <iomanip>
#include <io.h>
#include <fcntl.h>
#include "../true.h"
#include <sstream>

using namespace std;


double f(double x);
double h;
ostringstream s;

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

double u_cal(double u, int n) { 
    double temp = u; 
    for (int i = 1; i < n; i++) 
        temp = temp * (u - i); 
    return temp; 
} 

int fact(int n){
   return (!n) || (n == 1) 
   ? 1 
   : n * fact(n - 1);
}

void r1(const Coords c, double **table, int start, int end) {
   if (start == end) cout << "y0 + ";
   else {
      r1(c, table, start, end - 1);
      printf("p");
      for (int i = start + 1; i < end; i++) {
         printf("(p-%d)", i);
      } 
      printf("(y%d/%d!) + ", end, end);
   }
}

void r2(const Coords c, double **table, int start, int end) {
   if (start == end) cout << c[start].y << " + ";
   else {
      r2(c, table, start, end - 1);
      if (table[0][end]) {
         for (int i = start; i < end; i++) {
            if (!i) cout << "(" << s.str() << ")";
            else cout << "(" << s.str() << "-" << i << ")";
         } 
         
         printf("(%.6g/%d) + ", table[0][end], fact(end));
      }
   }
}

void r3(const Coords c, double **table, int start, int end) {
   if (start == end) cout << c[start].y << " + ";
   else {
      r3(c, table, start, end - 1);
      if (table[0][end]) {
         for (int i = start; i < end; i++) {
            if (!i) cout << "(" << s.str() << ")";
            else cout << "(" << s.str() << "-" << i << ")";
         } 
         
         printf("%.6g + ", table[0][end] / fact(end));
      }
   }
}

double f(double x) {
   return
   /* f(x): */ log(x + 1)
   ;
}

int main() {

   const int n =
   /* terms: */ 6
   ;

   const Coords c = {
      // x values (or {x, y} pairs):
      {0, 0}, {2, 4}, {4, 56}, {6, 204}, {8, 496}, {10, 980}
   };

   double x =
   /* x to approximate: */ 3
   ;

   // cout << fixed << showpoint << setprecision(6);
   // cout << "true value: " << f(x) << endl;


   h = c[1].x - c[0].x;
   if (!c[0].x && h != 1) s << "x/" << h;
   else if (c[0].x && h == 1) s << "(x-" << c[0].x << ")";
   else if (c[0].x && h != 1) s << "((x/" << h << ")" << "-" << c[0].x << ")";
   else s << "x";
   cout << "p = (x-x0) / h" << endl;
   printf("p = (x-%.6g) / %.6g\n\n", c[0].x, (c[1].x - c[0].x));

   double **table = new double *[n];

   for (int i = 0; i < n; i++) {
      table[i] = new double[n];
      table[i][0] = c[i].y;
   }

   for (int i = 1; i < n; i++)
      for (int j = 0; j < n - i; j++)
            table[j][i] = table[j + 1][i - 1] - table[j][i - 1];

   cout << "forward difference table: " << endl;
   for (int i = 0; i < n; i++) {
        cout << c[i].x << "\t";
        for (int j = 0; j < n - i; j++)
            cout << table[i][j] << "\t";
        cout << endl;
    }

   cout << "formula: ";
   r1(c, table, 0, n - 1);
   cout << endl << "f(x) = ";
   r2(c, table, 0, n - 1);
   cout << endl << "f(x) = ";
   r3(c, table, 0, n - 1);

   double sum = table[0][0]; 
   double u = (x - c[0].x) / (c[1].x - c[0].x); 

   for (int i = 1; i < n; i++) { 
      sum = sum + (u_cal(u, i) * table[0][i]) / 
                              fact(i); 
   } 

   printf("\nvalue at f(%.6g) = %.6g", x, sum);
   return 0;
}