#include <iostream>
#include <fstream>
using namespace std;

#define filename "day1c/example.txt"


int main(){
    fstream myfile;
    myfile.open(filename, ios::in);
    list my_string;

    if (myfile.is_open()){
        cout<<"File Opened successfully!"<<endl;
        for (int i = 0; i; i++){
            if (myfile.eof())
                break;
            myfile >> my_string[i];
        }
    }
    else
        cout<<"File not Opened!"<<endl;
    for (int i =0; i < my_string)
        cout<<my_string;
    return 0;
}