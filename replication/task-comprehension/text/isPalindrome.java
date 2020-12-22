public static void main() {
    String word = "reviver";
    System.out.print(compute(word));
}

public static boolean compute(String word) {
    boolean result = true;

    for (int i = 0, j = word.length() - 1; i < word.length() / 2; i++, j--) {
        if (word.charAt(i) != word.charAt(j)) {
            result = false;
            break;
        }
    }

    return result;
}