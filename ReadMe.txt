
PDF Document Classifier

### Overview:
Both algorithms are designed to classify a PDF document into predefined categories based on keyword matches, but they use different approaches to achieve this goal.

### Algorithm 1: Naive Document Classification
1. **Approach**:
   - The first algorithm uses a straightforward method where it reads the PDF document, extracts the text, and then processes it.
   - It counts how many times each word in the document matches keywords from each category.
   - After counting the matches, it selects the category with the highest keyword match count as the document's predicted category.

2. **Steps**:
   - Extracts text from the PDF.
   - Converts the text to lowercase and splits it into words.
   - Compares each word with predefined category keywords.
   - Classifies the document into the category with the highest number of matches.

3. **Efficiency**:
   - The algorithm directly compares each word in the document with the category keywords, making it slower as the number of words and categories increases.

4. **Use Case**:
   - Suitable for small documents with a limited number of categories and keywords.

---

### Algorithm 2: Optimized Document Classification
1. **Approach**:
   - This algorithm uses an optimized technique called "Inverted Index" to classify the document.
   - It creates an inverted index that maps each keyword to its related categories.
   - Then, it processes the document and checks if words in the document are present in the inverted index.
   - The algorithm counts how many times each category appears based on keyword matches and chooses the category with the highest match count.

2. **Steps**:
   - Extracts text from the PDF.
   - Processes the text and splits it into words.
   - Builds an inverted index that maps keywords to categories.
   - Checks for keyword matches using the inverted index, increasing the match count for related categories.
   - Classifies the document into the category with the highest match count.

3. **Efficiency**:
   - The inverted index reduces the number of comparisons needed, making it more efficient, especially for larger documents and a greater number of categories.
   - The inverted index allows for faster keyword lookups, improving performance as the data scales.

4. **Use Case**:
   - Ideal for handling larger datasets with more categories and keywords, as it is more scalable and efficient.

---

### Key Differences:
1. **Efficiency**:
   - Keyword Matching (Naive Document Classification) performs direct word matching, which can be slower for larger datasets.
   - Inverted Index (Optimized Document Classification) uses an inverted index for fast lookups, making it more efficient as the number of categories and keywords increases.

2. **Complexity**:
   - Keyword Matching (Naive Document Classification) is simpler and easier to implement but less efficient for larger datasets.
   - Inverted Index (Optimized Document Classification) is more complex due to the creation of the inverted index but offers better performance and scalability.

3. **Scalability**:
   - Keyword Matching (Naive Document Classification) might struggle with scalability as it checks every word in the document against every category's keywords.
   - Inverted Index (Optimized Document Classification) is better suited for scalability because the inverted index allows for quicker matches.

4. **Use Case**:
   - Keyword Matching (Naive Document Classification) is more suitable for small documents with fewer categories.
   - Inverted Index (Optimized Document Classification) is better for larger documents and more categories, offering improved speed and accuracy.

---

In conclusion, while both algorithms are useful for classifying documents based on keywords, Inverted Index offers better performance and scalability for larger datasets, making it a more suitable choice for real-world applications.
