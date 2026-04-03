import java.util.Scanner;

public class e1073 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        for(int i=2; i<=x; i++){
            if(i%2==0){
                int resultado = (int) Math.pow(i, 2);
                System.out.printf("%d^2 = %d\n", i, resultado); 
            }
        }
        sc.close();
    }
}
