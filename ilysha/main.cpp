#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale.h>
#include <vector>
using namespace std;
void test(vector<vector<double>>, int, vector<double>, vector<double>);

void gauss(vector<vector<double>> a, vector<double> b, int n) {
	for (int k = 0; k < n; k++) {
        if (k == n - 1)
            break;
		for (int i = k + 1; i < n; i++) {
            if (!a[k][k]) {
                for (int j = k + 1; j < n; j++) {
                    if (a[j][k]) {
                        swap(a[k], a[j]);
                        swap(b[k], b[j]);
                    }
                    break;
                }
            }
			double cn = a[i][k] / a[k][k];
			a[i][k] = 0;
			b[i] -= b[k] * cn;
			for (int j = k + 1; j < n; j++) {
				a[i][j] -= a[k][j] * cn;
			}
		}
	}

	vector<double> x(n, 0);
	x[n - 1] = b[n - 1] / a[n - 1][n - 1];
	if (x[n - 1] != x[n - 1]) {
        cout << "Система не решаема!" << endl;
        return;
	}
	for (int i = n - 2; i >= 0; i--) {
		double sum = 0;
		for (int j = i + 1; j < n; j++) {
			sum += a[i][j] * x[j];
        }
		x[i] = (b[i] - sum) / a[i][i];
	}
	cout << "Получившиеся корни: ";
	for (int i = 0; i < n; i++)
        cout << setprecision(15) << x[i] << " ";
	cout << endl;
	test(a, n, x, b);
	return;
}

void test(vector<vector<double>> a, int n, vector<double> x, vector<double> b) {
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
	vector<vector<double>> a(n, vector<double>(n));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			a[i][j] = rand() % 10;

	vector<double> b(n);
	for (int i = 0; i < n; i++)
		b[i] = rand() % 10;

	gauss(a, b, n);
	return 0;
}
