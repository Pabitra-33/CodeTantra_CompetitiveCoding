#include<bits/stdc++.h>
using namespace std;

int fibo(int n)
{
    if(n <= 1){
        return n;
    }
    return fibo(n-1) + fibo(n-2);
}

int countWays(int steps){
    return fibo(steps+1);
}

int main(){
    int steps;
    cin >> steps;
    cout<<countWays(steps);
    return 0;
}
