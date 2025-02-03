#include <iostream>


void addInterest(float balance, float rate) {
    balance += balance * rate;
    std::cout << "New balance: " << balance << std::endl;
    std::cout << "Address of balance: " << &balance << std::endl;
}

int main() {
    float amount = 1000;
    float rate = 0.05;
    addInterest(amount, rate);
    std::cout<< "Balance after interest: " << amount << std::endl;
    return 0;
}