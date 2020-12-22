public static void main() {
    int n = 3247;
    System.out.print(compute(n));
}

public static int compute(int number) {
    if (number == 0) {
        return 0;
    }

    return (number % 10) + compute((int) number/10);
}