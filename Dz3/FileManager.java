package HomeWork.Dz3;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
public class FileManager {
    /**
     * Прочитываем файл
     * @param filePath путь к файлу
     * @return Текст который находится в файле
     * @throws IOException
     */
    public String readFile(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new FileNotFoundException("Файл не найден");
        }

        StringBuilder content = new StringBuilder();

        try (FileReader reader = new FileReader(file)) {
            int character;
            while ((character = reader.read()) != -1) {
                content.append((char) character);
            }
        }

        return content.toString();
    }

    /**
     *  Запись в файл
     * @param filePath путь к файлу
     * @param content что записываем
     * @throws IOException
     */
    public void writeFile(String filePath, String content) throws IOException {
        File file = new File(filePath);

        try (FileWriter writer = new FileWriter(file)) {
            writer.write(content);
        }
    }

    /**
     * Копирование файла в директорию/файл
     * @param sourceFilePath это какой файл берем
     * @param destinationFilePath это куда файл копируем
     * @throws IOException
     */
    public void copyFile(String sourceFilePath, String destinationFilePath) throws IOException {
        File sourceFile = new File(sourceFilePath);
        if (!sourceFile.exists()) {
            throw new FileNotFoundException("Исходный файл не найден");
        }

        File destinationFile = new File(destinationFilePath);

        try (FileReader reader = new FileReader(sourceFile);
             FileWriter writer = new FileWriter(destinationFile)) {
            int character;
            while ((character = reader.read()) != -1) {
                writer.write(character);
            }
        }
    }
}
