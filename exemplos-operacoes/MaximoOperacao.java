public class MaximoOperacao implements Operacao {
    @Override
    public int executar(int[] dados) {
        int max = dados[0];
        for (int i = 1; i < dados.length; i++) {
            if (dados[i] > max) {
                max = dados[i]
            }
         }
    }
        return max;
}


