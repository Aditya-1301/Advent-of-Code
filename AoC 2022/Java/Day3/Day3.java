package Day3;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class Day3 {
    public static void prioritySum() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(
                new FileReader("D:\\AdventOfCode2022\\src\\Day3\\input3.txt"));
        HashMap<Character,Integer> h = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            h.put((char) ('a'+i),i+1);
        }
        for (int i = 0; i < 26; i++) {
            h.put((char) ('A'+i),i+27);
        }
        String s;
        int Psum = 0;
        while ((s = bufferedReader.readLine())!=null){
            String s1,s2;
            StringBuilder s01 = new StringBuilder(),s02 = new StringBuilder();
            for (int i = 0; i < s.length()/2; i++) {
                s01.append(s.charAt(i));
            }
            for (int i = s.length()/2; i < s.length(); i++) {
                s02.append(s.charAt(i));
            }
            char c = repeatedCharBetweenThe2Strings(s01.toString(),s02.toString());
            Psum += h.get(c);
        }
        System.out.println(Psum);
    }

    public static char repeatedCharBetweenThe2Strings(String s, String s1){
        char retVal = 0;
        A:
        for (int i = 0; i < s.length(); i++) {
            B:
            for (int j = 0; j < s1.length(); j++) {
                if(s.charAt(i) == s1.charAt(j)){
                    retVal = s.charAt(i);
                    break A;
                }
            }
        }
        return retVal;
    }

    public static void prioritySum2() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(
                new FileReader("D:\\AdventOfCode2022\\src\\Day3\\input3.txt"));
        HashMap<Character,Integer> h = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            h.put((char) ('a'+i),i+1);
        }
        for (int i = 0; i < 26; i++) {
            h.put((char) ('A'+i),i+27);
        }
        String s;
        int Psum = 0;
        ArrayList<String> strings = new ArrayList<>();
        while ((s = bufferedReader.readLine())!=null){
            strings.add(s);
        }
        System.out.println(strings);
        for (int i = 0; i < strings.size() - 2 ; i+=3) {
            char c = repeatedCharBetweenThe3Strings(strings.get(i), strings.get(i+1),strings.get(i+2));
            Psum += h.get(c);
        }
        System.out.println(Psum);
    }

    public static char repeatedCharBetweenThe3Strings(String s, String s1,String s2){
        char retVal = 0;
        boolean a = false;
        A:
        for (int i = 0; i < s.length(); i++) {
            B:
            for (int j = 0; j < s1.length(); j++) {
                if(s.charAt(i) == s1.charAt(j)){
                    C:
                    for (int k = 0; k < s2.length(); k++) {
                        if(s.charAt(i) == s2.charAt(k)){
                            retVal = s.charAt(i);
                            a = true;
                            break A;
                        }
                    }
                }
            }
        }
        System.out.println(a);
        return retVal;
    }

    public static void main(String[] args) throws IOException {
        prioritySum2();
    }
}
