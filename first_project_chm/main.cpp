#include <iostream>
#include <vector>
#include <locale.h>
#include <iomanip>
#include <cmath>
using namespace std;
const double E = 0.00001e-5;

bool convergnc(vector<double> a, int n, int k) {
    double sum = 0;
    for (int i = 0; i < n; i++)
        if (i != k)
            sum += fabs(a[i]);
    return fabs(a[k]) >= sum ? 1 : 0;
}

void swap_distance(vector<vector<double>> &a, int l, int r) {
    for (int i = l; i < (l + r) / 2; i++)
        swap(a[i], a[r-i-1]);
}

bool swap_and_check(vector<vector<double>> a, vector<double> b, int n) {
    for (int i = 0; i < n; i++) {
        if (convergnc(a[i], n, )) {
            swap(a[i], a[k]);
            swap(b[i], b[k]);
            return 1;
        }
    }
    return 0;
}

void shuffle(vector<vector<double>> a, vector<double> b, int n) {

}

void relax_method(vector<vector<double>> a, vector<double> b, vector<double> &x, int n) {
    double w = 0.5;
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
            mx = xkp[i] - x[i] < mx ? mx : xkp[i] - x[i];
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
            a[i][j] = rand() % 10;
    vector<double> b(n);
    for (int i = 0; i < n; i++)
        b[i] = rand() % 10;
    vector<double> x(n, 1);

    for (int i = 0; i < n; i++) {
        double sum = 0;
        for (int j = 0; j < n; j++)
            if (j != i)
                sum += fabs(a[i][j]);
        if (fabs(a[i][i]) < sum) {
            bool f = shuffle(0, a, ba);
            if (f)
                break;
            else {
                cout << "Условие сходимости не выполняется.";
                return 0;
            }
        }
    }

    relax_method(a, b, x, n);
    test(a, b, x, n);
    return 0;
}
