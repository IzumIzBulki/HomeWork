package HomeWork.Dz3;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        FileManager fileManager = new FileManager();
        fileManager.writeFile("G:\\exeption\\lesson1\\src\\homeworks\\hw3\\file.txt", " Вот оно!");
        fileManager.copyFile("G:\\exeption\\lesson1\\src\\homeworks\\hw3\\file.txt", "G:\\exeption\\lesson1\\src\\homeworks\\hw3\\file1.txt");
        System.out.println(fileManager.readFile("G:\\exeption\\lesson1\\src\\homeworks\\hw3\\file1.txt"));
    }
}
