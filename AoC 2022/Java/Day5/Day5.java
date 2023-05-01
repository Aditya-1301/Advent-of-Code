package Day5;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class Day5 {
    public static LinkedList<String>[] setup(){
        LinkedList<String>[] l = new LinkedList[9];
        String [] s  = new String[9];
        for (int i = 0; i < l.length; i++) {
            l[i] = new LinkedList<>();
        }
        s[0] = "TRGWQMFP";
        s[1] = "RFH";
        s[2] = "DSHGVRZP";
        s[3] = "GWFBPHQ";
        s[4] = "HJMSP";
        s[5] = "LPRSHTZM";
        s[6] = "LMNHTP";
        s[7] = "RQDF";
        s[8] = "HPLNCSD";
        for (int i = 0; i <s.length ; i++) {
            for (int j = 0; j <s[i].length() ; j++) {
                try{
                l[i].add(String.valueOf(s[i].charAt(j)));
                }catch (Exception e){
                    System.out.println(e);
                }
            }
        }
        for (int i = 0; i < l.length; i++) {
            System.out.println(l[i]);
        }
        return l;
    }

    public static void operate(LinkedList<String>[] l) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(
                "D:\\AdventOfCode2022\\src\\Day5\\input5.2.txt"
        ));
        String s;
        while (( s = bufferedReader.readLine()) !=null){
            String[] splited = s.split("\\s+");
            int n = Integer.parseInt(splited[1]);
            int a = Integer.parseInt(splited[3]);
            int b = Integer.parseInt(splited[5]);
            for (int i = 0; i < n; i++) {
                l[b-1].addFirst(l[a-1].remove());
            }
        }
        for (int i = 0; i < l.length; i++) {
            System.out.println(l[i]);
        }
    }

    public static void operate2(LinkedList<String>[] l) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(
                "D:\\AdventOfCode2022\\src\\Day5\\input5.2.txt"
        ));
        String s;
        while (( s = bufferedReader.readLine()) !=null){
            String[] splited = s.split("\\s+");
            int n = Integer.parseInt(splited[1]);
            int a = Integer.parseInt(splited[3]);
            int b = Integer.parseInt(splited[5]);
            LinkedList<String> l1 = new LinkedList<>();
            for (int i = 0; i < n; i++) {
                l1.add(l[a-1].remove());
            }
            //Collections.reverse(l1);
            for (int i = 0; i < n; i++) {
                l[b-1].addFirst(l1.removeLast());
            }
            l[b-1].addAll(l1);
        }
        for (int i = 0; i < l.length; i++) {
            System.out.println(l[i]);
        }
    }

    public static void main(String[] args) throws IOException {
        LinkedList<String>[] l = setup();
        System.out.println("\n\n\n\n");
        operate2(l);
    }
}

//TPGVQPFDH

//DMRDFRHHH
