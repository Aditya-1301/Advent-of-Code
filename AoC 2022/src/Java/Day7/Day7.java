package Java.Day7;

import com.sun.source.tree.Tree;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day7 {
    static class TreeStructure{
        int size;
        String name;
        TreeStructure prev;
        ArrayList<TreeStructure> directories;
        HashMap<String, Integer> files;

        TreeStructure(String name){
            this.size = 0;
            this.name = name;
            this.directories = new ArrayList<>();
            this.files = new HashMap<>();
        }

        void addToDirectoryList(String name){
            TreeStructure dir = new TreeStructure(name);
            dir.prev = this;
            this.directories.add(dir);
        }

        void addToFileMap(String file_name, int file_size){
            this.files.put(file_name, file_size);
        }

        HashMap<String, Integer> allDirectorySizes(){
            HashMap<String, Integer> dirMap = new HashMap<>();
            TreeStructure current = this;
            dirMap.put(current.name, current.size);
            if(!current.directories.isEmpty()){
                for (var i: current.directories) {
                    dirMap.put(i.name, i.size);
                }
            }
            return dirMap;
        }

        int setSize(){
            int totalSum = 0;
            TreeStructure current = this;
            if(!current.files.isEmpty()){
                int dirSum = 0;
                for (int i: current.files.values()) {
                    dirSum += i;
                }
                current.size = dirSum;
                totalSum += dirSum;
            }
            if (!current.directories.isEmpty()) {
                for (var i : current.directories) {
                    int dirSum = i.setSize();
                    i.size = dirSum;
                    totalSum += dirSum;
                }
            }
            this.size = totalSum;
            return totalSum;
        }

        /*
        @Override
        public String toString() {
            TreeStructure current = this;
            StringBuilder fileTree = new StringBuilder("Dir(" + current.name + ") :");
            if (current.directories.isEmpty()){
                System.out.println("Dirs Empty: Current Value for current var = ( " + current.name + " )");
                if(!current.files.isEmpty()){
                    fileTree.append("Files: ");
                    for (var i: current.files.entrySet()) {
                        fileTree.append("(" + i.getKey() + ":" + i.getValue() + ") " + " | ");
                    }
                    fileTree.append("\n");
                }
            }
            else{
                System.out.println("Dirs Full: Current Value for current var = ( " + current.name + " )");
                for (var i: current.directories) {
                    current = i;
                    fileTree.append(current.toString());
                    fileTree.append("Dir: " + i.name + "\n");
                    if(!i.files.isEmpty()){
                        fileTree.append("\t-> Files: ");
                        for (var j: i.files.entrySet()) {
                            fileTree.append("(" + j.getKey() + ":" + j.getValue() + ") " + " | ");
                        }
                        fileTree.append("\n");
                    }
                }
            }
            return fileTree.toString();
            }
        }
        */

        @Override
        public String toString() {
            TreeStructure current = this;
            StringBuilder fileTree = new StringBuilder("{ Dir(" + current.name + "): ");
            if (!current.directories.isEmpty()){
                fileTree.append(current.directories);
            }
            fileTree.append(Arrays.toString(current.files.entrySet().toArray()));
            fileTree.append(" }");
            return fileTree.toString();
        }
    }


    public static void parseFileTree(TreeStructure root) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(
                "D:\\Advent_Of_Code\\AoC 2022\\src\\Java\\Day7\\testInput.txt"));
        System.out.println("\n\n");
        Pattern pattern1 = Pattern.compile("\\$ cd (.+)$");
//        Pattern pattern2 = Pattern.compile("\\$ ls$");
        Pattern pattern3 = Pattern.compile("^dir\\s(\\w+)$");
        Pattern pattern4 = Pattern.compile("^(\\d+)\\s(\\w+(?:\\.\\w+)?)$");


        TreeStructure current = root;

        String s;
        bufferedReader.readLine();
        while( (s = bufferedReader.readLine()) != null ){
            Matcher matcher1 = pattern1.matcher(s);
//            Matcher matcher2 = pattern2.matcher(s);
            Matcher matcher3 = pattern3.matcher(s);
            Matcher matcher4 = pattern4.matcher(s);
            if (matcher1.matches()){
                if (matcher1.group(1).equals("..") && current.name != "\\") {
                    System.out.println("Changed Directory to Dir(" + current.prev.name + ") from Dir(" + current.name + ")");
                    current = current.prev;
                }
                else{
                    for (var i: current.directories) {
                        if (Objects.equals(i.name, matcher1.group(1))){
                            System.out.println("Changed Directory to Dir(" + i.name + ") from Dir(" + current.name + ")");
                            current = i;
                        }
                    }
                }
            }
            if(matcher3.matches()){
                current.addToDirectoryList(matcher3.group(1));
                System.out.println("Added Dir(" + matcher3.group(1)+ ") to Dir(" + current.name + ")");
            }
            if (matcher4.matches()){
                current.addToFileMap(matcher4.group(2), Integer.parseInt(matcher4.group(1)));
                System.out.println("Added [ File Name = " + matcher4.group(2) + ", Size = " + matcher4.group(1) + "] to Dir(" + current.name + ")");
            }
        }


        /*
            Matcher matcher1 = pattern1.matcher(s);
            Matcher matcher2 = pattern2.matcher(s);
            Matcher matcher3 = pattern3.matcher(s);
            Matcher matcher4 = pattern4.matcher(s);
            if (matcher1.matches()){
                System.out.println(1 + " " + matcher1.group(1) + " | " + s);
            }
            if(matcher2.matches()){
                System.out.println(2 + " " + s  + " | " + s);
            }
            if(matcher3.matches()){
                System.out.println(3 + " " + matcher3.group(1)  + " | " + s);
            }
            if(matcher4.matches()){
                System.out.println(4 + " " + matcher4.group(0) + " " + matcher4.group(1)  + " | " + s);
            }
        */
    }
    public static void main(String[] args) throws IOException {
        TreeStructure root = new TreeStructure("\\");

        parseFileTree(root);

        System.out.println("\n\n\n");
        System.out.println(root);

        System.out.println(root.setSize());

        System.out.println(root.size);
        System.out.println();
        System.out.println(Arrays.toString(root.allDirectorySizes().entrySet().toArray()));
        // a -> 94269 ; e -> 584;  d -> 24933642; / -> [a+e+d : 25028495] + [files: 23352670]; Total: 48381165

    }
}
