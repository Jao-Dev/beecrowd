import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class e1175 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> n = new ArrayList<>();

        for(int i=0; i<20; i++){
            int x = sc.nextInt();
            n.add(x);
        }
        Collections.reverse(n);

        int y=0;
        for(int i:n){
            System.out.printf("N[%d] = %d\n",y,i);
            y+=1;
        }
        sc.close();
    }
}
