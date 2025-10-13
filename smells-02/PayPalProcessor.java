package CodeSmells2;

public class PayPalProcessor implements PaymentProcessor {

    @Override
    public void process(String customerName) {
        System.out.println("Processing PayPal for " + customerName);
    }
    
}
