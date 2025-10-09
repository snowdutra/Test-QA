package CodeSmells2;

public class CreditCardProcessor implements PaymentProcessor {

    @Override
    public void process(String customerName) {
        System.out.println("Processing credit card for " + customerName);
    }
    
}
