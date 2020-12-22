public static void main() {
    String text = "The quick brown fox jumps";
    System.out.print(compute(text));
}

public static int compute(String text) {
    int result = 0;

    boolean flag = false;
    for (int i = text.length() - 1; i >= 0; i--) {
        char c = text.charAt(i);
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            flag = true;
            result++;
        } else {
            if (flag)
                break;
        }
    }

    return result;
}