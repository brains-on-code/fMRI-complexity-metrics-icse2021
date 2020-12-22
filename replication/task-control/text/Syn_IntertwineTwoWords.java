public String find(String word1, String word2) {
    String intertwinedWord = "";

    if (word1.length() == word2.length()) {
        for (int i = 0; i < word1.length(); i++) {
            intertwinedWord = intertwinedWord + word1.charAt(i)
                    + word2.charAt(i);
        }
    }

    return intertwinedWord;
}