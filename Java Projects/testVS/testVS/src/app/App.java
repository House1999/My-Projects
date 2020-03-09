package app;

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello Java");

        int[][][] matrice3D = new int[3][5][6];
        System.out.println(Arrays.deepToString(matrice3D));
    }
}