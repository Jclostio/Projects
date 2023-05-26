import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.Random;
import java.util.Scanner;

public class Solver {

    public static void menu() throws FileNotFoundException {
        String lettersNotInWord = ""; // Initial String variables
        String lettersInWordKnown = "_____"; // for the letters in the word that are green (known position)
        String lettersInWordUnknown = "_____"; // for the letters in the word that are yellow (unknown position)

        LinkedList<String> wordList = getWords();
        LinkedList<String> wordList2 = getWords();

        boolean flag = true;
        Random rand = new Random();

        while(flag) {
            wordList = solve(wordList, wordList2, lettersNotInWord, lettersInWordKnown, lettersInWordUnknown);
            if(wordList.size() > 75) {
                String word = wordList.get(rand.nextInt(wordList.size()));

                Set<Character> uniqueChars = new HashSet<>();
                Boolean repeatedChars = false;
                for (char c : word.toCharArray()) {
                    if (uniqueChars.contains(c)) {
                        repeatedChars = true; // if there are repeated characters
                        break;
                    }
                    uniqueChars.add(c);
                }
                if(repeatedChars) {
                    continue;
                } else {
                    System.out.println("Try: " + word);
                }
            }
            else if(wordList.size() == 1){
                System.out.println("The word is: " + wordList.toString());
                return;
            }
            else if(wordList.size() == 0) {
                System.out.println("Couldn't get the word...");
                return;
            }
            else {
                System.out.println("Try: " + wordList.toString());
            }
            Scanner inputObj = new Scanner(System.in);
            System.out.println("Which letters were not in the word? (type exit to quit): ");
            lettersNotInWord += inputObj.nextLine();
            if(lettersNotInWord.contains("exit")) {
                System.exit(0);
            }
            System.out.println("Which letters were in the word (yellow)? (___x_): ");
            lettersInWordUnknown = inputObj.nextLine();
            System.out.println("Which letters were in the word (green)? (_x___): ");
            lettersInWordKnown = inputObj.nextLine();
        }

    }
    private static LinkedList<String> solve(LinkedList<String> wordList, LinkedList<String> wordList2, String lettersNotInWord, String lettersInWordKnown, String lettersInWordUnknown) {

        for(String word : wordList) { //remove words from wordList that have a letter that isn't in the word
            for(int i = 0; i < lettersNotInWord.length(); i++) {
                char letter = lettersNotInWord.charAt(i);
                if(word.contains("" + letter)) {
                    wordList2.remove(word);
                    break;
                }
            }
        }
        wordList = (LinkedList<String>) wordList2.clone(); //for the yellow letters, if the letter is '_' do nothing
        for(String word : wordList) {
            for(int i = 0; i < lettersInWordUnknown.length(); i++) {
                char letter = lettersInWordUnknown.charAt(i);
                if(letter == '_') {
                    continue;
                }
                if(!word.contains("" + letter) || (word.indexOf(letter) == lettersInWordUnknown.indexOf(letter))) { //if the letter is in the wrong spot, or doesn't contain the letter, remove the word from the linked list
                    wordList2.remove(word);
                    break;
                }
            }
        }
        wordList = (LinkedList<String>) wordList2.clone(); //for the green letters, same as previous conditional statement.
        for(String word : wordList) {
            for(int i = 0; i < lettersInWordKnown.length(); i++) {
                char letter = lettersInWordKnown.charAt(i);
                if(letter == '_') {
                    continue;
                }
                if(!word.contains("" + letter) || (word.indexOf(letter) != lettersInWordKnown.indexOf(letter))) {
                    wordList2.remove(word);
                    break;
                }
            }
        }
        wordList = (LinkedList<String>) wordList2.clone();
        return wordList;
    }

    private static LinkedList<String> getWords() throws FileNotFoundException {
        LinkedList<String> wordList = new LinkedList<String>();
        File file = new File("C:\\Users\\jacob\\Desktop\\Projects\\Wordle Solver\\src\\wordsBig.txt");
        Scanner inputFile = new Scanner(file);
        while(inputFile.hasNext()) {
            wordList.add(inputFile.nextLine());
        }
        inputFile.close();
        return wordList;
    }

}
