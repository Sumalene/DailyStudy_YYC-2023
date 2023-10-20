package sample;

//设计一个银行帐户类，成员变量包括账号、储户姓名、开户时间、身份证号码、存款余额等帐户信息，成员方法包括存款、取款操作。

class BankAccount {
    private String account;
    private String name;
    private String time;
    private String id;
    private double balance;

    public BankAccount(String account, String name, String time, String id, double balance) {
        this.account = account;
        this.name = name;
        this.time = time;
        this.id = id;
        this.balance = balance;
    }

    public BankAccount() {
    }

    public void deposit(double money) {
        balance += money;
    }

    public void withdraw(double money) {
        balance -= money;
    }

    public void show() {
        System.out.println("账号：" + account);
        System.out.println("姓名：" + name);
        System.out.println("开户时间：" + time);
        System.out.println("身份证号码：" + id);
        System.out.println("存款余额：" + balance);
    }
}

public class BankStart {
    BankAccount bankAccount = new BankAccount("123456", "张三", "2020-10-10", "123456789", 1000);

    public static void main(String[] args) {
        BankStart bankStart = new BankStart();
        bankStart.bankAccount.show();
        bankStart.bankAccount.deposit(100);
        bankStart.bankAccount.show();
        bankStart.bankAccount.withdraw(200);
        bankStart.bankAccount.show();
    }
}
