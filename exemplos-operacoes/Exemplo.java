public class Exemplo {
    public static void imprimirDados(Pessoa pessoa) {
        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Idade: " + pessoa.getIdade());
        System.out.println("Endereço: " + pessoa.getEndereco());
    }

    public int executarOperacaoSobreDados(int[] dados, Operacao operacao) {
        if (dados == null) {
            throw new IllegalArgumentException("dados == null");
        }
        if (dados.length == 0) {
            throw new IllegalArgumentException("dados.length == 0");
        }
        return operacao.executar(dados);
    }

}