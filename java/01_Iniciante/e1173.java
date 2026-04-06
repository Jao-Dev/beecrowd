import java.util.Scanner;

public class e1173 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = 0;
        int cont = 0;

        while(y<10){
            System.out.printf("N[%d] = %d\n",cont,x);
            
            x*=2;
            cont+=1;
            y+=1;
        }
        sc.close();
    }
}
