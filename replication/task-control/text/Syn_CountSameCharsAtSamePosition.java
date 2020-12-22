public int find(String word1, String word2) {
	int shortestLength;

	if (word1.length() < word2.length())
		shortestLength = word1.length();
	else
		shortestLength = word2.length();

	int sameCharsAtSamePosition = 0;

	for (int i = 0; i < shortestLength; i++) {
		if (word1.charAt(i) == word2.charAt(i)) {
			sameCharsAtSamePosition++;
		}
	}

	return sameCharsAtSamePosition;
}