#include <iostream>
using namespace std;

#define LOG(x) cout<<x<<endl

class Persona{


    private:
    int priv;


    public:
    int all;

Persona(){
    priv=10;
    all=20;
}

int getAll(){
    return this->all;
}

int getPriv(){
    LOG(this);
    return this->priv;
}

};



int main(){
        // int x=0;
        // int* px;
        // px=&x;
        // LOG(*px);
        // LOG(&x);

        Persona p1;
        Persona* ptrp=&p1;
        //int* prueba= &p1.getAll();
        LOG(p1.getAll());
        LOG(ptrp->getAll());
        LOG(p1.getPriv());
        LOG(ptrp);



    return 0;
}