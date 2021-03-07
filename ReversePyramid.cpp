#include <iostream>

using namespace std;


class ReversePyramid {
    private:
        int rows;
    public:
        ReversePyramid(int r) {
            rows = r;
        }
    
    void printPyramid() {
        for(int i=1;i<=rows;i++){
            for(int j=1;j<i;j++){
                cout<<" ";
            }
            for(int j=rows-i;j>=0;j--){
                cout<<"*";
            }
            for(int j=rows-i;j>0;j--){
                cout<<"*";
            }
            cout<<"\n";
        }
    }
    
    ~ReversePyramid(){
    }
};

class ChildReversePyramid : public ReversePyramid {
    public:
        ChildReversePyramid(int r) : ReversePyramid(r){
            
        }
};
int main()
{
    int ro;
    cout<<"Enter the number of rows: ";cin>>ro;
    cout<<"\n";
    ChildReversePyramid obj(ro);
    obj.printPyramid();
    return 0;
}
