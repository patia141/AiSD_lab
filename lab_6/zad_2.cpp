#include <iostream>

using namespace std;

void sortowanie(int *tab, int n)
{
    int pom;
    for(int i=0;i<n-1;i++) {
        for(int j=0;j<n-i-1;j++)
            if(tab[j]>tab[j+1]) {
                pom=tab[j];
                tab[j]=tab[j+1];
                tab[j+1]=pom;
            }
    }
}

int main()
{
    int n = 5;
    int tab[n] = {5,8,12,-4,-7};
    sortowanie(tab,n);
    int rozp = tab[n-1]-tab[0];
    cout<<"Rozpietosc to: "<<rozp;
    return 0;
}
