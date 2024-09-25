
#include <iostream>
#include <vector>
#include <set>
using namespace std;
int main()
{
    int x;
    int num;
    cin>>x;
    vector<int>a(x);
    vector<int>b(x);
    
    for(int i=0;i<x;i++){
        cin>>num;
        a[i]=num;
    }
    for(int i=0;i<x;i++){
        cin>>num;
        b[i]=num-1;
    }
    
    vector<int> c(x);
    for(int i=0;i<x;i++){
        c[b[i]]=a[i];
    }
    
    for(int i=0;i<x;i++) cout<<c[i]<<" ";
    
    return 0;
}
