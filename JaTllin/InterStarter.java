package sample;

//创建—个名为MyInterface的接口，它是继承了MySuperInterface1和MySuperInterface2两个接口的子接口。之后再写一个具体类实现MyInterface接口。

interface MySuperInterface1{
    void method1();
}

interface MySuperInterface2{
    void method2();
}

interface MyInterface extends MySuperInterface1,MySuperInterface2{
    void method3();
}


public class InterStarter {
    public static void main(String[] args) {

        MyInterface myInterface = new MyInterface() {
            @Override
            public void method1() {
                System.out.println("This is method1");
            }

            @Override
            public void method2() {
                System.out.println("This is method2");
            }

            @Override
            public void method3() {
                System.out.println("This is method3");
            }
        };
        myInterface.method1();
        myInterface.method2();
        myInterface.method3();
    }
}
