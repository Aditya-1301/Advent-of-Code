package Day8;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Day8 {
    public static Integer VisibleTrees() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("D:\\AdventOfCode2022\\src\\Day8\\input8.txt"));
        //Scanner sc = new Scanner("D:\\AdventOfCode2022\\src\\Day8\\input8.txt");
        Integer [][] trees = new Integer[100][100];
        int count = 0;
        String s;
        while ((s = bufferedReader.readLine()) != null){

        }
        //while (sc.hasNext()){
            //String s = sc.next();

        //}
        for (int i = 0; i < trees.length; i++) {
            for (int j = 0; j < trees.length; j++) {
                System.out.print(trees[i][j] + "\t");
            }
            System.out.println();
        }

        return null;
    }

    public static void main(String[] args) throws IOException {

    }
}
