#include <iostream>

using namespace std;

int main()
{
    int n = 5;
    int tab[n] = {2,8,-3,7,-6};
    int suma = 0;
    for(int i=0; i<n; i+=2) suma += tab[i];
    cout<<"Suma to: "<<suma;
    return 0;
}
