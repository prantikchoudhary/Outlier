import java.util.Scanner;

public class TextAnalyzerBetter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the text: ");
        String text = scanner.nextLine().trim();
        scanner.close();

        int palindromeCount = 0;
        int fullStopCount = 0;
        int commaCount = 0;
        int specialCharCount = 0;
        int sentenceCount = 0;
        int paragraphCount = 0;

        // Splitting into paragraphs
        String[] paragraphs = text.isEmpty() ? new String[0] : text.split("\\n+");
        paragraphCount = paragraphs.length;

        for (String paragraph : paragraphs) {
            // Splitting into sentences
            String[] sentences = paragraph.split("[.!?]");
            sentenceCount += sentences.length;

            for (String sentence : sentences) {
                // Splitting into words
                String[] words = sentence.trim().split("\\s+");

                for (String word : words) {
                    // Checking for palindromes with only alphabetic characters
                    String cleanedWord = word.replaceAll("[^a-zA-Z]", "").toLowerCase();
                    if (!cleanedWord.isEmpty() && isPalindrome(cleanedWord)) {
                        palindromeCount++;
                    }

                    // Modifying words starting with an uppercase letter
                    if (word.length() > 0 && Character.isUpperCase(word.charAt(0))) {
                        word = Character.toLowerCase(word.charAt(0)) + word.substring(1).toUpperCase();
                    }

                    // Counting special characters
                    for (char c : word.toCharArray()) {
                        if (!Character.isLetterOrDigit(c)) {
                            specialCharCount++;
                        }
                    }
                }
            }

            // Counting full stops and commas
            for (char c : paragraph.toCharArray()) {
                if (c == '.') {
                    fullStopCount++;
                } else if (c == ',') {
                    commaCount++;
                }
            }
        }

        // Outputting the results
        System.out.println("Total Palindrome Words: " + palindromeCount);
        System.out.println("Total Full Stops: " + fullStopCount);
        System.out.println("Total Commas: " + commaCount);
        System.out.println("Total Special Characters: " + specialCharCount);
        System.out.println("Total Sentences: " + sentenceCount);
        System.out.println("Total Paragraphs: " + paragraphCount);
    }

    public static boolean isPalindrome(String word) {
        int left = 0, right = word.length() - 1;
        while (left < right) {
            if (word.charAt(left) != word.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
