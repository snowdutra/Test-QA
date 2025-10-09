public class OperacaoSoma implements Operacao {
	@Override
	public int executar(int r, int dado) {
		r += dado;
		return r;
	}
}
