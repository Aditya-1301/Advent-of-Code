package Day1;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Day1 {
    public static void FindCaloriesFromInput() throws IOException {
        ArrayList<Integer> a = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(
        new FileReader("D:\\Advent_Of_Code\\AoC 2022\\Java\\Day1\\input1.txt"));
        String s;
        int sum = 0;
        while ((s = bufferedReader.readLine())!=null){
            if(s.length() == 0 || s.charAt(0) =='\n'){
                a.add(sum);
                sum = 0;
            }
            else{
                sum += Integer.parseInt(s);
            }
        }
        System.out.println(a);
        Collections.sort(a);
        int sum1 = 0;
        for (int i = a.size() - 3; i <a.size() ; i++) {
            sum1 += a.get(i);
        }
        System.out.println(sum1);
        System.out.println(Collections.max(a));
    }
    public static void main(String[] args) throws IOException {
        FindCaloriesFromInput();
    }
}
