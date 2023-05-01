package Day4;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

public class Day4 {
    public static void OverlappingIDs() throws FileNotFoundException {
        Scanner sc = new Scanner( new File("D:\\AdventOfCode2022\\src\\Day4\\inputAltered.txt") ) ;
        int OverlapCount = 0;
        int [][] rangeValues = new int[100][4];

        Outer_While_Loop:
        while (sc.hasNext()){
            int [] r  = new int[4];
            for (int i = 0; i < r.length; i++) {
                r[i] = sc.nextInt();
            }

            //Used for PART 1 of the Question
            /*
            if((r[0]<=r[2] && r[1]>=r[3]) || (r[0]>=r[2] && r[1]<=r[3])){
                OverlapCount++;
            }
            */

            //The Hashsets part is for the PART 2 of the Question
            HashSet<Integer> h1 = new HashSet<>();
            for(int i = r[0]; i <= r[1]; i++){
                h1.add(i);
            }
            HashSet<Integer> h2 = new HashSet<>();
            for(int i = r[2]; i <= r[3]; i++){
                h2.add(i);
            }
            for (int i = 1; i <= 99; i++) {
                if(h1.contains(i) && h2.contains(i)){
                    OverlapCount++;
                    continue Outer_While_Loop;
                }
            }

        }
        System.out.println(OverlapCount);
    }

    public static void main(String[] args) throws FileNotFoundException {
        OverlappingIDs();
    }
}

//boolean mark [] = new boolean[100];
//Arrays.fill(mark,false);
//            int noOverlapMarkCount = r[3] - r[2] + r[1] - r[0] + 2;
//            for (int i = 0; i < r.length; i++) {
//                mark[r[i]] = true;
//            }
//            int markTrueCount = 0;
//            for (int i = 0; i < mark.length; i++) {
//                if(mark[i]==true){
//                    markTrueCount++;
//                }
//            }
//            if(markTrueCount == noOverlapMarkCount){
//                continue;
//            }
//            else OverlapCount++;
