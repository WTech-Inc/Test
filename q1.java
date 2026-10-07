abstract class Customer {
    protected String name;

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
    public abstract double getDiscount();
}

// 2. Walk-in 客人類別 (繼承 Customer)
class WalkInCustomer extends Customer {
    public WalkInCustomer(String name) {
        super(name);
    }

    @Override
    public double getDiscount() {
        return 0.0;
    }
}

class MemberCustomer extends Customer {
    private double discount;

    public MemberCustomer(String name, double discount) {
        super(name);
        this.discount = discount;
    }

    @Override
    public double getDiscount() {
        return discount;
    }
}

class Billing {
    public static void printInvoice(Customer c, double amount) {
        System.out.println("Thank you! " + c.getName());
        double discount = c.getDiscount();
        
        if (discount > 0) {
            System.out.println("The discount for " + c.getName() + " is " 
                + (int)(discount * 100) + "%");
        }
        
        System.out.println("The discounted price is $" + amount * (1 - discount));
    }
}

public class Q1 {
    public static void main(String[] args) {
        Customer c1 = new WalkInCustomer(""); 
        Customer c2 = new MemberCustomer("Remi Cheung", 0.1線);

        Billing.printInvoice(c1, 1500);
        Billing.printInvoice(c2, 1500);
    }
}