package CodeSmells2;

public class OrderProcessor {
	private String customerName;

	// Corrigir o code smell Primitive Obsession
	private OrderProduct[] products;

	public OrderProcessor(String customerName, OrderProduct[] products) {
		this.customerName = customerName;
		this.products = products;
	}

	// Corrigir o code smell Switch Statements
	public void processPayment(PaymentProcessor paymentProcessor) {
		paymentProcessor.process(customerName);
	}
}
