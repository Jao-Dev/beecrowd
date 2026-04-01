import java.util.Arrays;
import java.util.Scanner;

public class e1045 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double[] x = new double[3];
        for(int i=0; i<x.length; i++){x[i] = sc.nextDouble();};

        Arrays.sort(x);
        double a = x[2];
        double b = x[1];
        double c = x[0];

        if(a>=b+c){System.out.println("NAO FORMA TRIANGULO");}
        else{
            if(a*a == (b*b + c*c)){System.out.println("TRIANGULO RETANGULO");}
            if(a*a > (b*b + c*c)){System.out.println("TRIANGULO OBTUSANGULO");}
            if(a*a < (b*b + c*c)){System.out.println("TRIANGULO ACUTANGULO");}
            if(a==b && b==c){System.out.println("TRIANGULO EQUILATERO");}
            else if(a==b || a==c || b==c){System.out.println("TRIANGULO ISOSCELES");}
        }
        sc.close();
    }
}
