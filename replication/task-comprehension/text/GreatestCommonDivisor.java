public static void main() {
    int number1 = 20;
    int number2 = 15;
    System.out.print(compute(number1, number2));
}

public static int compute(int number1, int number2) {
    int temp = number1;

    while (temp != 0) {
        if (number1 < number2) {
            temp = number1;
            number1 = number2;
            number2 = temp;
        }
        temp = number1 % number2;
        if (temp != 0) {
            number1 = number2;
            number2 = temp;
        }
    }

    return number2;
}