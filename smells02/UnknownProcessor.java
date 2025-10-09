package CodeSmells2;

public class UnknownProcessor implements PaymentProcessor {

    @Override
    public void process(String customerName) {
        System.out.println("Unknown payment method!");
    }
    
}
