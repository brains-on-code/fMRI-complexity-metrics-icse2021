public int[] find(int[] arrayToSort) {
    for (int i = 0; i < arrayToSort.length; i++) {
        for (int j = i; j > 0; j--) {
            if (arrayToSort[j - 1] > arrayToSort[j]) {
                int swapVariable = arrayToSort[j];
                arrayToSort[j] = arrayToSort[j - 1];
                arrayToSort[j - 1] = swapVariable;
            }
        }
    }

    return arrayToSort;
}
