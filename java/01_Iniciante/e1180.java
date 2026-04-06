import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class e1180 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int in = sc.nextInt();
        ArrayList<Integer> y = new ArrayList<>();

        for(int i=0;i<in;i++){
            int x = sc.nextInt();
            y.add(x);
        }

        int min = Collections.min(y);
        int pos = y.indexOf(min);

        System.out.printf("Menor valor: %d\n",min);
        System.out.printf("Posicao: %d\n",pos);

        sc.close();
    }
}
