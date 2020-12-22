public String find(int number) {
    String result = "";

    while (number > 0) {
        if (number % 2 == 0) {
            result = "0" + result;
        } else {
            result = "1" + result;
        }

        number = number / 2;
    }

    return result;
}