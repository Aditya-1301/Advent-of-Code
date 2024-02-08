package Java.Day7;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day7 {
    /*
    root_Folder : TreeStruct = {
        List[Dirs: TreeStruct{} ...],
        Map[File_Size: File_Name, ...]
    }
    */
    static class TreeStructure{

        int size;
        String name;
        TreeStructure prev;
        ArrayList<TreeStructure> directories;
        HashMap<String, Integer> files;

//        TreeStructure(){
//            this.name = "";
//            this.directories = new ArrayList<>();
//            this.files = new HashMap<>();
//        }

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

        int getSize(){
            TreeStructure current = this;
            if (current.directories.isEmpty()){
                if(!current.files.isEmpty()){
                    int sum = 0;
                    for (int i: current.files.values()) {
                       sum += i;
                    }
                    this.size = sum;
                }
            }
            else{
                int sum = 0;
                for (var i: current.directories) {
                    sum += i.getSize();
                    if(!i.files.isEmpty()){
                        for (int j: i.files.values()) {
                            sum += j;
                        }
                    }
                    this.size = sum;
                }
            }
            return this.size;
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

        void setSize(){
            int totalSum = 0;
            TreeStructure current = this;
            if (current.directories.isEmpty()){
                if(!current.files.isEmpty()){
                    int dirSum = 0;
                    for (int i: current.files.values()) {
                        dirSum += i;
                    }
                    current.size = dirSum;
                    totalSum += current.size;
                }
            }
            else{
                for (var i: current.directories) {
                    int dirSum = i.getSize();
                    if(!i.files.isEmpty()){
                        for (int j: i.files.values()) {
                            dirSum += j;
                        }
                    }
                    current.size = dirSum;
                    totalSum += current.size;
                }
            }
            this.size = totalSum;
        }

        @Override
        public String toString() {
            TreeStructure current = this;
            StringBuilder fileTree = new StringBuilder("ROOT: " + current.name + "\n");
            if (current.directories.isEmpty()){
                System.out.println("FLAG");
//                if(!current.files.isEmpty()){
//                    fileTree.append("Files: ");
//                    for (var i: current.files.entrySet()) {
//                        fileTree.append("(" + i.getKey() + ":" + i.getValue() + ") " + " | ");
//                    }
//                    fileTree.append("\n");
//                }
            }
            else{
                System.out.println("FLAG2");
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
            if(!current.files.isEmpty()){
                fileTree.append("Files: ");
                for (var i: current.files.entrySet()) {
                    fileTree.append("(" + i.getKey() + ":" + i.getValue() + ") " + " | ");
                }
                fileTree.append("\n");
            }
            return fileTree.toString();
        }
    }



    public static void parseFileTree() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(
                "D:\\Advent_Of_Code\\AoC 2022\\src\\Java\\Day7\\testInput.txt"));
        String s;

        Pattern pattern1 = Pattern.compile("\\$ cd (.+)$");
        Pattern pattern2 = Pattern.compile("\\$ ls$");
        Pattern pattern3 = Pattern.compile("^dir\\s(\\w+)$");
        Pattern pattern4 = Pattern.compile("^(\\d+)\\s(\\w+(?:\\.\\w+)?)$");
        //                for(int i = 0; i < root.directories.size(); i++){
        //                    TreeStructure dir = root.directories.get(i);
        //                    if (dir.name.equals(matcher1.group(1))){
        //
        //                    }
        //                }
        ArrayList<String> input = new ArrayList<>();
        TreeStructure root = new TreeStructure("\\");
        bufferedReader.readLine();
        TreeStructure current = root;
        while( (s = bufferedReader.readLine()) != null ){
//            input.add(s);
            System.out.println(s);
            Matcher matcher1 = pattern1.matcher(s);
//            Matcher matcher2 = pattern2.matcher(s);
            Matcher matcher3 = pattern3.matcher(s);
            Matcher matcher4 = pattern4.matcher(s);
            if (matcher1.matches()){
                if (matcher1.group(1).equals("..") && current.name != "\\") {
                    System.out.println("Current = " + current.name);
                    current = current.prev;
                }
                else{
                    for (var i: current.directories) {
                        if (Objects.equals(i.name, matcher1.group(1))){
                            current = i;
                            System.out.println("Current = " + current.name);
                        }
                    }
//                    root.directories.add(new TreeStructure(matcher1.group(1)));
                }
//                System.out.println(1 + " " + matcher1.group(1) + " | " + s);
            }
//            if(matcher2.matches()){
//                System.out.println(2 + " " + s  + " | " + s);
//            }
            if(matcher3.matches()){
                current.addToDirectoryList(matcher3.group(1));
                System.out.println("Added to dir: " + current.name);
//                System.out.println(3 + " " + matcher3.group(1)  + " | " + s);
            }
            if (matcher4.matches()){
                current.addToFileMap(matcher4.group(2), Integer.parseInt(matcher4.group(1)));
                System.out.println("Added to dir: " + current.name + ", file " + matcher4.group(2) + " of size " + matcher4.group(1));
            }
        }

        System.out.println(root);
        root.setSize();
        System.out.println(root.getSize());
        System.out.println();
        System.out.println(Arrays.toString(root.allDirectorySizes().entrySet().toArray()));
//        for (int i = 0; i < input.size() - 1; i++) {
//            if(input.get(i+1).equals("$ cd ..\n")){
//
//            }
//        }

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
        parseFileTree();
    }
}
