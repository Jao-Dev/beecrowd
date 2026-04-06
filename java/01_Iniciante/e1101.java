import java.util.ArrayList;
import java.util.Scanner;

public class e1101 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();

        while (m>0&&n>0) {
            int soma = 0;
            ArrayList<Integer> ls = new ArrayList<>();
            
            if(m>n){
            for(int i=n; i<=m; i++){
                soma+=i;
                ls.add(i);
            }
            }
            else if(n>m){
                for(int i=m; i<=n; i++){
                    soma+=i;
                    ls.add(i);
                }
            }
            
            for(int i = 0; i < ls.size(); i++) {
                if(i > 0) System.out.print(" ");
                System.out.print(ls.get(i));
            }
            System.out.printf(" Sum=%d\n", soma);

            m = sc.nextInt();
            n = sc.nextInt();
        }

        sc.close();
    }
}
