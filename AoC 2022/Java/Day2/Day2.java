package Day2;

import java.io.*;
import java.util.HashMap;

public class Day2 {

    public static void strategyGuide() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(
                new FileReader("D:\\AdventOfCode2022\\src\\Day2\\input2.txt"));
        HashMap<String,Integer> hashMap = new HashMap<>();
        hashMap.put("A X",1+3);
        hashMap.put("A Y",2+6);
        hashMap.put("A Z",3+0);
        hashMap.put("B X",1+0);
        hashMap.put("B Y",2+3);
        hashMap.put("B Z",3+6);
        hashMap.put("C X",1+6);
        hashMap.put("C Y",2+0);
        hashMap.put("C Z",3+3);
        String s;
        int sum = 0;
        while ((s = bufferedReader.readLine())!= null){
            if(hashMap.containsKey(s)){
                sum +=hashMap.get(s);
            }
        }
        System.out.println(sum);
    }
    public static void strategyGuide2() throws IOException {
        //X->LOSE ; Y->DRAW ; Z->WIN
        BufferedReader bufferedReader = new BufferedReader(
                new FileReader("D:\\AdventOfCode2022\\src\\Day2\\input2.txt"));
        HashMap<String,Integer> hashMap = new HashMap<>();
        hashMap.put("A X",3+0);
        hashMap.put("A Y",1+3);
        hashMap.put("A Z",2+6);
        hashMap.put("B X",1+0);
        hashMap.put("B Y",2+3);
        hashMap.put("B Z",3+6);
        hashMap.put("C X",2+0);
        hashMap.put("C Y",3+3);
        hashMap.put("C Z",1+6);
        String s;
        int sum = 0;
        while ((s = bufferedReader.readLine())!= null){
            if(hashMap.containsKey(s)){
                sum +=hashMap.get(s);
            }
        }
        System.out.println(sum);
    }
    public static void main(String[] args) throws IOException {
        strategyGuide2();
    }
}
