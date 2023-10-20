package sample;

abstract class Person {
    abstract void pay();
}
class Teacher extends Person {
    int basicSalary;
    int classHour;

    Teacher(int basicSalary, int classHour) {
        this.basicSalary = basicSalary;
        this.classHour = classHour;
    }

    @Override
    void pay() {
        System.out.println("工资支出=" + (basicSalary + classHour * 30));
    }
}
class CollegeStudent extends Person {
    int scholarship;

    CollegeStudent(int scholarship) {
        this.scholarship = scholarship;
    }

    @Override
    void pay() {
        System.out.println("奖学金支出=" + scholarship);
    }
}

class Example05_2 {
    public static void main(String args[]) {
        Person p1 = new Teacher(1000, 10);
        Person p2 = new CollegeStudent(500);
        p1.pay();
        p2.pay();
    }
}

