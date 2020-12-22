static void find(String str1, String str2) {
    int n = str2.length();

    if (n == 0) {
        System.out.println(str1);
    } else {
        for (int i = 0; i < n; i++)
            compute(
                str1 + str2.charAt(i),
                str2.substring(0, i) + str2.substring(i + 1, n)
            );
    }
}