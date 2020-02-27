/*
 * A C++ program to test `src/greeting.cpp` file.
 * 
 * Command:
 * $ g++ greeting_test.cpp ../src/greeting.cpp -o greeting_test.exe


g++ greeting_test.cpp ../src/greeting.cpp -c

g++ greeting_test.o ../src/greeting.cpp -o -L/usr/lib/ -llibhello.so greeting_test.exe

 */

#include <iostream>
#include <string>
#include "../src/greeting.h"

//#include "libhello.h"


int main() {
    std::string result = helloUser( "John" );

    std::cout << result << std::endl;
/*
  int z =0;

z=sum(50);
    std::cout << z << std::endl;
  */
}