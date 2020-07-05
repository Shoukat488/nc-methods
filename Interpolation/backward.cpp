#define _USE_MATH_DEFINES
#include <math.h>
#include <iostream>
#include <iomanip>
#include "../true.h"
#include <sstream>

using namespace std;


double f(double x);
double h;
int n;
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
        temp *= (u + i); 
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
   if (start == end) cout << c[n - 1].y << " + ";
   else {
      r2(c, table, start, end - 1);
      if (table[n - 1][end]) {
         for (int i = start; i < end; i++) {
            if (!i) cout << "(" << s.str() << ")";
            else cout << "(" << s.str() << "-" << i << ")";
         } 
         
         printf("(%.6g/%d) + ", table[n - 1][end], fact(end));
      }
   }
}

void r3(const Coords c, double **table, int start, int end) {
   if (start == end) cout << c[n - 1].y << " + ";
   else {
      r3(c, table, start, end - 1);
      if (table[n - 1][end]) {
         for (int i = start; i < end; i++) {
            if (!i) cout << "(" << s.str() << ")";
            else cout << "(" << s.str() << "-" << i << ")";
         } 
         
         printf("%.6g + ", table[n - 1][end] / fact(end));
      }
   }
}

double f(double x) {
   return
   /* f(x): */ log(x + 1)
   ;
}

int main() {

   n =
   /* terms: */ 5
   ;

   const Coords c = {
      // x values (or {x, y} pairs):
      // x values (or {x, y} pairs):
      {1.0, 0.7651977}, {1.3, 0.6200860}, {1.6, 0.4554022},
      {1.9, 0.2818186}, {2.2, 0.1103623}
   };

   double x =
   /* x to approximate: */ 57
   ;

   h = c[1].x - c[0].x;
   if (!c[n - 1].x && h != 1) s << "x/" << h;
   else if (c[n - 1].x && h == 1) s << "(x-" << c[n - 1].x << ")";
   else if (c[n - 1].x && h != 1) s << "((x-" << c[n - 1].x << ")" << "/" << h << ")";
   else s << "x";
   cout << "p = (x-x" << n - 1 << ") / h" << endl;
   printf("p = (x-%.6g) / %.6g\n\n", c[n - 1].x, (c[1].x - c[0].x));

   double **table = new double *[n];

   for (int i = 0; i < n; i++) {
      table[i] = new double[n];
      table[i][0] = c[i].y;
   }

   for (int i = 1; i < n; i++)
      for (int j = n - 1; j >= i; j--)
            table[j][i] = table[j][i - 1] - table[j - 1][i - 1];

   cout <<"backward difference table: " << endl;
   cout << "x" << "\t";
   for (int i = 0; i < n; i++)
      cout << "y" << i << "\t";
   cout << endl;
   for (int i = 0; i < n; i++) {
        cout << c[i].x << "\t";
        for (int j = 0; j <= i; j++)
            cout << table[i][j] << "\t";
        cout << endl;
    }
   cout << endl;

   cout << "formula: ";
   r1(c, table, 0, n - 1);
   cout << endl << "f(x) = ";
   r2(c, table, 0, n - 1);
   cout << endl << "f(x) = ";
   r3(c, table, 0, n - 1);

   double sum = table[n - 1][0]; 
   double u = (x - c[n - 1].x) / (c[1].x - c[0].x); 

   for (int i = 1; i < n; i++)
      sum = sum + (u_cal(u, i) * table[n - 1][i]) / fact(i); 

   printf("\nvalue at f(%.6g) = %.6g", x, sum);
   return 0;
}