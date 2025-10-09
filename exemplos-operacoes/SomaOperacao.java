public class SomaOperacao implements Operacao {
    @Override
    public int executar( int[] dados) {
        int r = 0;
        for (int valor : dados) {
            r += valor;
        }
        return r;
    }

}
