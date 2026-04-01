import java.util.Arrays;
import java.util.Scanner;

public class e1042 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] x = new int[3];

        for (int i=0; i<x.length; i++){x[i] = sc.nextInt();};
        int[] copiaX = Arrays.copyOf(x, x.length);
        Arrays.sort(x);
        
        for (int i : x){System.out.println(i);};
        System.out.println("");
        for (int i : copiaX){System.out.println(i);};
        
        sc.close();
    }
}
