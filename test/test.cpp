#include <iostream>
#include <string>


class Student {
    private:
        int id;  //f Личный идентификатор студента
        std::string name;  //f Имя студента
    public:
        /*m Инициализация экземпляра класса Студент*/
        void init(int i, std::string n)
        {
             id = i;
             name = n;
        }

        /*m Вывод информации о студенте в консоль*/
        void display()
        {
             std::cout << id << "  " << name << std::endl;
        }
};

class Teacher {
    private:
        int id;  //f Личный идентификатор преподавателя
        std::string name;  //f Имя преподавателя
    public:
        /*m Инициализация экземпляра класса Преподаватель*/
        void init(int i, std::string n)
        {
             id = i;
             name = n;
        }

        /*m Вывод информации о преподавателе в консоль*/
        void display()
        {
             std::cout << id << "  " << name << std::endl;
        }
};

/*func Возвращает сумму двух целых чисел*/
int sum(int a, int b)
{
    return a + b;
}

/*func Возвращает разность двух целых чисел*/
int dif(int a, int b)
{
    return a - b;
}

int main(void) {
    Student s1; // создание объекта
    Student s2;
    s1.init(1, "Ivan");
    s2.init(2, "Oleg");
    s1.display();
    s2.display();
    std::cout << sum(10, 5) << std::endl;
    std::cout << dif(10, 5) << std::endl;
    return 0;
}