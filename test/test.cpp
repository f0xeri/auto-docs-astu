#include <iostream>
#include <string>


class Student {
    private:
        int id;  //f ������ ������������� ��������
        std::string name;  //f ��� ��������
    public:
        /*m ������������� ���������� ������ �������*/
        void init(int i, std::string n)
        {
             id = i;
             name = n;
        }

        /*m ����� ���������� � �������� � �������*/
        void display()
        {
             std::cout << id << "  " << name << std::endl;
        }
};

class Teacher {
    private:
        int id;  //f ������ ������������� �������������
        std::string name;  //f ��� �������������
    public:
        /*m ������������� ���������� ������ �������������*/
        void init(int i, std::string n)
        {
             id = i;
             name = n;
        }

        /*m ����� ���������� � ������������� � �������*/
        void display()
        {
             std::cout << id << "  " << name << std::endl;
        }
};

/*func ���������� ����� ���� ����� �����*/
int sum(int a, int b)
{
    return a + b;
}

/*func ���������� �������� ���� ����� �����*/
int dif(int a, int b)
{
    return a - b;
}

int main(void) {
    Student s1; // �������� �������
    Student s2;
    s1.init(1, "Ivan");
    s2.init(2, "Oleg");
    s1.display();
    s2.display();
    std::cout << sum(10, 5) << std::endl;
    std::cout << dif(10, 5) << std::endl;
    return 0;
}