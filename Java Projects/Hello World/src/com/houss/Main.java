package com.houss;

import org.w3c.dom.ls.LSOutput;

import java.awt.*;
import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.Date;


public class Main {

    public static void main(String[] args) {
        byte myAge = 30;
        long viewsCount = 3_123_456_789L;                // Pour separer les valeurs pour une meilleure lecture
        float price = 10.99F;
        char letter = 'A';
        boolean isEligible = false;
        
        
        byte age = 30;
        Date now = new Date();
        System.out.println(now);

        Point point1 = new Point(1,1);
        Point point2 = point1;
        point1.x = 2;

        System.out.println(point2);
        
        String message = "Hello ";
        message += "Buse!";
        System.out.println(message);
        System.out.println(message.endsWith("Buse"));
        System.out.println(message.length());
        System.out.println(message.indexOf("Buse"));
        System.out.println(message.replace("!", " <3"));
        System.out.println(message);
        message = message.replace("!", " <3");
        System.out.println(message);

        String message1 = "   Hey !   ";
        System.out.println(message1);
        System.out.println(message1.trim());

        String message3 = "Hello \"Buse\"";
        System.out.println(message3);

        int[] numbers = {1,2,3,4,5,6};
        int[] liste2 = new int[5];
        liste2[0] = 1;
        liste2[1] = 2;
        liste2[2] = 3;
        liste2[4] = 5;

        boolean[] liste3 = new boolean[4];

        liste3[2] = true;

        System.out.println("Length = " +numbers.length);

        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        System.out.println("Avec Array : "+Arrays.toString(liste2));
        System.out.println("Avec Array : "+Arrays.toString(liste3));

        Arrays.sort(liste2);
        System.out.println(Arrays.toString(liste2));

        // Matrices

        int[][] matrice = new int[2][3];

        matrice[0][0] = 1;

        System.out.println(Arrays.deepToString(matrice));  // DEEPTOSTRING pour les matrices

        int[][] matrice2 = {{1,2,3},{4,5,6}};
        System.out.println(Arrays.toString(matrice2));

        // Matrices 3D

        int[][][] matrice3D = new int[2][3][5];
        matrice3D[0][0][1] = 2;

        System.out.println(Arrays.deepToString(matrice3D));

        final float PI = 3.14F;  // Final  == constante
        // PI = 1; ==> Erreur

        int result = 10 + 3;
        System.out.println(result);

        // Division comme en C#

        System.out.println(10/3);
        System.out.println((double)10 / (double)3);


        result++;

        int x = 1;
        int y = x++; // ==> y = x puis x = x + 1 ==> x = 2, y =1
        int z = ++x; // ==> x++ puis y = x ==> x = y = 2

        int res = 10 + 3 * 2; // ==> 16 pas 26
        int res2 = (10 + 3) * 2; // ==> 26 pas 16

        short a = 1;
        int b = a + 2; // implicit casting, automatic casting, a est transforme en int puis le calcul se fait (automaticoment)
        System.out.println(b);

        // Implicit casting ==> pas perte d'info ==> byte > short > int > long > float > double

        double c = 1.1;
        double d = x + 2; // le int 2 est cast en double (2.0)

        // Explicit casting ==> perte d'info

        double t = 1.1;
        int r = (int)t + 2;
        System.out.println(r);

        String x2 = "1";
        int y2 = Integer.parseInt(x2) + 2;
        System.out.println(y2);
;
    }
}
