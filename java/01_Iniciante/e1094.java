import java.util.Scanner;

public class e1094 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int coelhos = 0;
        int ratos = 0;
        int sapos = 0;

        for(int i=0; i<x; i++){
            int qtd = sc.nextInt();
            String tipo = sc.next();
            
            if (tipo.equals("C")) {coelhos+=qtd;}
            else if (tipo.equals("R")) {ratos+=qtd;}
            else if (tipo.equals("S")) {sapos+=qtd;}
        }

        int total = coelhos+ratos+sapos;
        double pCoelhos = (coelhos*100.0)/total;
        double pRatos = (ratos*100.0)/total;
        double pSapos = (sapos*100.0)/total;

        System.out.printf("Total: %d cobaias\n", total);
        System.out.printf("Total de coelhos: %d\n", coelhos);
        System.out.printf("Total de ratos: %d\n", ratos);
        System.out.printf("Total de sapos: %d\n", sapos);

        if (total>0) {
            System.out.printf("Percentual de coelhos: %.2f %%%n", pCoelhos);
            System.out.printf("Percentual de ratos: %.2f %%%n", pRatos);
            System.out.printf("Percentual de sapos: %.2f %%%n", pSapos);
        }
        else{System.out.println("");}
    
        sc.close();
    }
}
