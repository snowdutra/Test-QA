package CodeSmells2;

public class BankTransferProcessor implements PaymentProcessor {

    @Override
    public void process(String customerName) {
        System.out.println("Processing bank transfer for " + customerName);
    }
    
}
