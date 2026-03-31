import java.util.Locale;
import java.util.Scanner;

public class e1021 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double x = sc.nextDouble();
        int[] notas = {100, 50, 20, 10, 5, 2};
        int[] moedas = {50, 25, 10, 5, 1};
        int valor = (int) x;
        
        System.out.println("NOTAS:");
        for (int i : notas){
            double qtd = valor/i;
            System.out.printf("%.0f nota(s) de R$ %d.00\n", qtd, i);
            valor %= i;
        }

        int valor2 = (int) Math.round((x-(int)x)*100);
        
        System.out.println("MOEDAS:");
        System.out.printf("%d moeda(s) de R$ 1.00\n", valor);
        for (int i : moedas){
            double qtd = valor2/i;
            System.out.printf(Locale.US, "%.0f moeda(s) de R$ %.2f\n", qtd, i/100.0);
            valor2 %= i;
        }
        sc.close();
    }
}
