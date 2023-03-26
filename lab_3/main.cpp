#include <iostream>

using namespace std;

void wieza_hanoi(int n, char a, char b, char c)
{
    if(n>0)
    {
        wieza_hanoi(n-1,a,c,b);
        cout<<"Przenies krazek z patyka "<<a<<" na patyk "<<b<<endl;
        wieza_hanoi(n-1,c,b,a);
    }
    else cout<<"Brak problemu :)";
}

int main()
{
    wieza_hanoi(3,'A','B','C');
    return 0;
}
