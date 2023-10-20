package sample;

interface Sittable{
    void sit();
}
interface Lie{
    void sleep();
}
interface HealthCare{
    void massage();
}
class Chair implements Sittable{
    public void sit(){System.out.println("This is sit method");}
}
/*interface Sofa extends Sittable,Lie    //接口可以实现多重继承，用逗号相隔。
{
}*/
class Sofa extends Chair implements Lie,HealthCare//一个类既可以从父类中继承同时又可以实现多个接口。
{
    public void sleep(){   // 完善你的代码
        System.out.println("This is sleep method");
    }
    public void massage(){   // 完善你的代码
        System.out.println("This is massage method");
    }
}

public class Example {
    public static void main(String args[]) {
        Sofa sofa = new Sofa();
        sofa.sit();
        sofa.sleep();
        sofa.massage();
    }
}
