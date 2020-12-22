public static void main() {
    int a = 3;
    int b = 2;
    System.out.print(compute(a, b));
}

static int compute(int a, int b) {
    if (b == 0) {
        return 1;
    }

    if (b == 1) {
        return a;
    }

    return (a + 1) * compute(a, b - 1);
}