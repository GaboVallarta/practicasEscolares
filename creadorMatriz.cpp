#include <iostream>
#include <vector>
using namespace std;

int main(){
    int h,a;
     int eleccion;
    bool cero=false;
    vector<int> matriz;

    cout<<"tamanio de matriz"<<endl;
    cin>>h>>a;
  
    
    elegir:
    cout<<"0,0 o 1,1 escribe 0 o 1"<<endl;
    cin>>eleccion;
    if(eleccion==0 || eleccion==1){
        if(eleccion==0){
            cero=true;
        }
    }else{
        cout<<"no"<<endl;
        goto elegir;
    }

    for(int i=0;i<=a*h;i++)matriz.push_back(0);
    
    for(int i=1;i<=a*h;i++){
        cout<<matriz[i]<<" ";
        if(i%a==0)cout<<endl;
        
    }
    int x,y;
    while(1){
        cout<<"coordenadas"<<endl;
        cin>>x>>y;
    
    if(!cero){
        y-=1;
    }else{
       
        x+=1;
    }
    matriz[a*y+x]=(matriz[a*y+x]+1)%2;

    for(int i=1;i<=a*h;i++){
        cout<<matriz[i]<<" ";
        if(i%a==0)cout<<endl;
    }
    }
    
    return 0;
}