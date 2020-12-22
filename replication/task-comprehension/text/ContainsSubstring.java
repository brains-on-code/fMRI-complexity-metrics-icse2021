public static void main() {
    String word1 = "Hamburg";
    String word2 = "burg";
    System.out.print(compute(word1, word2));
}

public static boolean compute(String word1, String word2) {
    boolean result = false;

    for (int i = 0; i < word1.length(); i++) {
        for (int j = 0; j < word2.length(); j++) {
            if (i + j >= word1.length())
                break;
            if (word1.charAt(i + j) != word2.charAt(j)) {
                break;
            } else {
                if (j == word2.length() - 1) {
                    result = true;
                    break;
                }
            }
        }
    }

    return result;
}