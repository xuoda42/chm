#include <iostream>
#include <vector>
#include <locale.h>
#include <iomanip>
#include <cmath>
using namespace std;
const double E = 1e-10; // Эпсилон

void relax_method(vector<vector<double>> a, vector<double> b, vector<double> &x, int n) {
    double w = 0.5; // Параметр релаксации
    double mx = -1;
    do {
        mx = -1;
        cout << "Корни, полученные методом Зейделя на итерации: ";
        vector<double> xk(n);
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) {
                if (j < i)
                    sum += a[i][j] * xk[j];
                else if (j > i)
                    sum += a[i][j] * x[j];
            }
            xk[i] = (b[i] - sum) / a[i][i];
            cout << setprecision(15) << xk[i];
            if (i != n - 1)
                cout << "; ";
            else
                cout << ".";
        }
        cout << endl << "Корни, полученные на итерации: ";
        vector<double> xkp(n);
        for (int i = 0; i < n; i++) {
            xkp[i] = w * xk[i] + (1 - w) * x[i];
            mx = fabs(xkp[i] - x[i]) < mx ? mx : fabs(xkp[i] - x[i]);
            cout << setprecision(15) << xkp[i];
            if (i != n - 1)
                cout << "; ";
            else
                cout << ".";
            //cout << setprecision(15) << mx << " ";
        }
        cout << endl << setprecision(15) << "Полученная максимальная разница: " << mx << endl << endl;
        x = xkp;
    } while (mx > E);
    return;
}

void test(vector<vector<double>> a, vector<double> b, vector<double> x, int n) {
    if (x[n - 1] != x[n - 1] || x[n - 1] == INFINITY || x[n - 1] == -INFINITY) {
        cout << "Система не имеет решения.";
        return;
    }
	cout << "Полученная разница: ";
	for (int i = 0; i < n; i++) {
		double sum = 0;
		for (int j = 0; j < n; j++) {
			sum += a[i][j] * x[j];
		}
		cout << setprecision(15) <<  b[i] - sum;
		if (i != n - 1)
                cout << "; ";
            else
                cout << ".";
	}
	return;
}

int main() {
    setlocale(LC_ALL, "Russian");
    int n;
    cin >> n;
    vector<vector<double>> a(n, vector<double>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> a[i][j];
    vector<double> b(n);
    for (int i = 0; i < n; i++)
        cin >> b[i];
    vector<double> x(n, 0);

    vector<int> ind(sizeof(a), -1);
    for (int i = 0; i < n; i++) {
        int mx = -1, q = -1;
        for (int j = 0; j < n; j++)
            if (fabs(a[i][j]) > mx) {
                mx = fabs(a[i][j]);
                q = j;
            }
        double sum = 0;
        for (int j = 0; j < n; j++)
            if (j != q)
                sum += a[i][j];
        if (mx >= sum && i > 0)
            for (int j = 0; j < i; j++) {
                if (ind[j] != q && j == i - 1)
                    ind[i] = q;
            }
        else if (mx >= sum && !i)
            ind[i] = q;
    }
    for (int i = 0; i < n; i++)
        if (ind[i] == -1) {
            cout << "Не соблюдены условия сходимости.";
            return 0;
        }
    for (int i = 0; i < n; i++) {
        if (ind[i] != i)
            for (int j = i + 1; j < n; j++)
                if (ind[j] == i) {
                    swap(ind[i], ind[j]);
                    swap(a[i], a[j]);
                    swap(b[i], b[j]);
                    break;
                }
    }

    relax_method(a, b, x, n);
    test(a, b, x, n);
    return 0;
}
