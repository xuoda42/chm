#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale.h>
using namespace std;

void caut(double** a, double* b, int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << setprecision(15) << a[i][j] << " ";
		cout << setprecision(15) << ": " << b[i] << endl;
	}
	cout << endl;
}

void swapString(double** a, double* b, int n, int f, int s) {
    double* cn = new double[n+1];
    for(int i = 0; i < n; i++) {
        cn[i] = a[f][i];
        a[f][i] = a[s][i];
    }
    cn[n] = b[f];
    b[f] = b[s];
    for (int i = 0; i < n; i++)
        a[s][i] = cn[i];
    b[s] = cn[n];
    cout << endl << "Переставим местами " << f << " и " << s << ": " << endl;
    caut(a, b, n);
    cout << endl;
    delete[] cn;
    return;
}

void gauss_triangle(double** a, double* b, int n) {
	for (int k = 0; k < n; k++) {
        if (k == n - 1)
            break;
		for (int i = k + 1; i < n; i++) {
            if (!a[k][k]) {
                for (int j = k + 1; j < n; j++) {
                    if (a[j][k])
                        swapString(a, b, n, k, j);
                    break;
                }
            }
			double cn = a[i][k] / a[k][k];
			a[i][k] = 0;
			b[i] -= b[k] * cn;
			for (int j = k + 1; j < n; j++) {
				a[i][j] -= a[k][j] * cn;
			}
			caut(a, b, n);
		}
	}
	return;
}

void gauss(double** a, int n, double* x, double* b) {
	x[n - 1] = b[n - 1] / a[n - 1][n - 1];
	if (x[n - 1] != x[n - 1]) {
        cout << "Система не решаема!" << endl;
        return;
	}
	//cout << setprecision(15) << "Получившиеся корни: " << x[n - 1] << " ";
	for (int i = n - 2; i >= 0; i--) {
		double sum = 0;
		for (int j = i + 1; j < n; j++) {
			sum += a[i][j] * x[j];
			//cout << j + 1 << ": "<< a[i][j] << " " << x[j] << " ";
        }
        //cout << sum << " ";
		x[i] = (b[i] - sum) / a[i][i];
		//cout << setprecision(15) << x[i] << " ";
	}
	cout << "Получившиеся корни: ";
	for (int i = 0; i < n; i++)
        cout << setprecision(15) << x[i] << " ";
	cout << endl;
	return;
}

void test(double** a, int n, double* x, double* b) {
    if (x[n - 1] != x[n - 1]) {
        return;
	}
	cout << "Полученная разница: ";
	for (int i = 0; i < n; i++) {
		double sum = 0;
		for (int j = 0; j < n; j++) {
			sum += a[i][j] * x[j];
		}
		cout << setprecision(15) <<  b[i] - sum << " ";
	}
	return;
}

int main() {
    srand(time(0));
    setlocale(LC_ALL, "Russian");
	int n;
	cin >> n;
	double** a = new double*[n];
	double** ba = new double*[n];
	for (int i = 0; i < n; i++) {
		a[i] = new double[n];
		ba[i] = new double[n];
		for (int j = 0; j < n; j++) {
			a[i][j] = rand() % 10;
			ba[i][j] = a[i][j];
		}
	}

	double* b = new double[n];
	double* bb = new double[n];
	for (int i = 0; i < n; i++) {
		b[i] = rand() % 10;
        bb[i] = b[i];
	}
    caut(a, b, n);

	gauss_triangle(a, b, n);

	double* x = new double[n];
	for (int i = 0; i < n; i++)
        x[i] = 0;
	gauss(a, n, x, b);

	test(ba, n, x, bb);

	for (int i = 0; i < n; i++)
		delete[] a[i];
	for (int i = 0; i < n; i++)
		delete[] ba[i];
	delete[] a;
	delete[] ba;
	delete[] b;
	delete[] bb;
	delete[] x;
	return 0;
}
