public static void main() {
    String input = "Yes";
    System.out.print(compute(input));
}

static Boolean compute(String input) {
    input = input.toLowerCase();

    if (input.contentEquals("n")) {
        return false;
    } else if (input.contentEquals("no")) {
        return false;
    }

    if (input.contentEquals("y")) {
        return true;
    } else if (input.contentEquals("yes")) {
        return true;
    }

    return null;
}