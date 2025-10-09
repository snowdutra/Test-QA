public class MediaOperacao implements Operacao {
    @Override
    public int executar(int[] dados) {
        int soma = 0;
        for (int valor : dados) {
            soma += valor;
        }
        return soma / dados.length;
    }
    
}
