#include <iostream>
#include <string>
#include <vector>

using namespace std;

int addNumbers(int num1, int num2){ //or void
    return num1 + num2;
}

double division(int a, int b){
    if (b == 0){
        throw "Division by zero error!";
    }
    return (a/b)
}

int main(){

    //PRINTING 
    cout << "Hello" << endl;
    cout << "World";
    cout << "!" << endl;

    //VARIABLES
    string name = "Mike";
    char testGrade = 'A';
    short age0 = 10;
    int age1 = 20; //unsigned by putting signed in front of it
    long age2 = 30; // 32-BIT SIGNED INTEGER
    long long age3 = 40; //64-BIT SIGNED INTEGER

    float gpa0 = 2.5f;
    double gp1 = 3.5;
    long double gpa2  = 3.5;

    bool isTall;
    isTall = true;

    name = "John";

    cout << "Your name is " << name << endl;

    //CONSTANTS

    int const BIRTH_YEAR = 1945; //cant switch it, convention is to be all caps
    cout << BIRTH_YEAR;

    //CASTING
    cout << (int)3.14 << endl;
    cout << (double)3 / 2 << endl;

    //POINTERS
    int num =10;
    cout << &num << endl;

    int *pNum = &num;
    cout << pNum << endl; //pnum references mem address (004FFDE0)
    cout << *pNum << endl; //*pNum dereferences mem address (10)

    //strings

    string greeting = "Hello"; // indexes: 01234

    cout << greeting.length() << endl;
    cout << greeting[0] << endl;
    cout << greeting.find ("llo") << endl;
    cout << greeting.find ("l") << endl;
    cout << greeting.substr(2) << endl;
    cout << greeting.substr(1,3) << endl;

    // NUMBERS

    cout << 2 * 3 << endl;
    cout << 10 % 3 << endl;
    cout << 1 + 2 * 3 << endl;
    cout << 10 / 3.0 << endl;

    int num = 10;
    num += 100;
    cout << num << endl;

    num++;
    cout << num << endl;

    //USER INPUT
    string name;
    cout << "Enter your name: ";
    cin >> name;
    cout << "Hello " << name << endl;

    int num1, num2;
    cout << "Enter first num: ";
    cin >> num1;
    cout << "Enter second num: ";
    cin >> num2;
    cout << "Answer: " << num1 + num2 << endl;

    //ARRAYS
    int luckyNumbers[6];
    int luckyNumbers[] = {4, 8, 15, 16, 23, 42}; //indexes: 0 1 2 3 4 5

    luckyNumbers[0] = 90;
    cout << luckyNumbers[0] << endl;
    cout << luckyNumbers[1] << endl;

    //N Dimnensional Arrays

    //int numberGrid[2][3];

    int numberGrid[2][3] = {{1,2,3}, {4,5,6}};
    numberGrid[0][1] = 99;

    cout << numberGrid[0][0] << endl;
    cout << numberGrid[0][1] << endl;

    //VECTOR
    vector<string> friends;
    friends.push_back("Oscar");
    friends.push_back("Angela");
    friends.push_back("Kevin");
    friends.insert(friends.begin() + 1, "Jim");

    friends.erase(friends.begin() + 1);
    cout << friends.at(0) << endl;
    cout << friends.at(1) << endl;
    cout << friends.at(2) << endl;
    cout << friends.size() << endl;

    int sum = addNumbers(4,60);
    cout << sum << endl;

    //IF STATEMENTS

    bool isStudent = false;
    bool isSmart = false;

    if (isStudent && isSmart){
        cout << "You are a student" << endl;
    } else if (isStudent && !isSmart){
        cout << "You are not a smart student" << endl;
    } else {
        cout << "You are not a student and not smart" << endl;
    }

    if (1 < 3) {
        cout << "number comparison was true" << endl;
    }

    if ('a' > 'b'){
        cout << "character comparison was true" << endl;
    }

    string myString = "cat";
    if (myString.compare("cat") == 0){
        cout << "string comparison was true" << endl;
    }

    //SWITCH STATEMENTS

    char myGrade = 'A';
    switch(myGrade){
        case 'A':
            cout << "You Pass" << endl;
            break;
        case 'F':
            cout << "You fail" << endl;
            break;
        default:
            cout << "Invalid grade" << endl;
    }

    //WHILE LOOPS

    int index = 1;
    while (index <= 5){
        cout << index << endl;
        index++;
    }

    for(int i = 0; i < 5; i++){
        cout << i << endl;
    }

    //EXCEPTION CATCHING

    try {
        division(10,0);
    } catch (const char* msg) {
        cerr << msg << endl;
    }









    return 0;

}

//OOP

class Book(
    public:
        string title;
        string author;

        void readBook(){
            cout << "Reading " + this->title + " by " + this->author << endl;
        }
)

int main()
{
    Book book1;
    book1.title = "Harry Potter";
    book1.author = "JK Rowling";

    book1.readBook();
}

//CONSTRUCTOR

class Book(
    public:
        string title;
        string author;

        Book(string title, string author){ //Constructor
            this->title = title;
            this->author = author;
        }

        void readBook(){
            cout << "Reading " + this->title + " by " + this->author << endl;
        }
)

int main()
{
    Book book1("Harry Potter", "JK Rowling")
    cout << book1.getTitle() << endl;

    return 0;
}


//GETTER AND SETTER
class Book(
    private:
        string title;
        string author;

        public:
        Book(string title, string author){ //Constructor
            this->title = setTitle;
            this->author = setAuthor;
        }

        string getTitle(){ //Accessor
            return this->title;
        }

        void setTitle(string title){ //Accessor
            this->title = title;
        }

        //same for author
)

int main()
{
    Book book1("Harry Potter", "JK Rowling")
    cout << book1.getTitle() << endl;

    return 0;
}


