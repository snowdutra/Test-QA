public class ClasseExemploResolvida {
	private int processarNumerosPares(int[] dados, Operacao operacao) {
		int r = 0;

		for (int i = 0; i < dados.length; i++) {
			if (dados[i] % 2 == 0) {
				r = operacao.executar(r, dados[i]);
			}
		}

		return r;
	}

	public int metodoExemplo(int[] dados, Operacao operacao, boolean todosOsCasos) {
		int r1 = 0;
		int r2 = 0;

		r1 = processarNumerosPares(dados, operacao);

		if (todosOsCasos) {
			for (int i = 0; i < dados.length; i++) {
				dados[i]++;
			}

			r2 = processarNumerosPares(dados, operacao);
		}

		return r1 + r2;
	}
}
