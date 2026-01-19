# Semantic Search
Semantic search in LLMs understands the meaning and context of a query, not just keywords, by using deep learning to convert words/phrases into numerical vectors (embeddings) that capture relationships, enabling it to find relevant information even with different wording, synonyms or paraphrased queries, leading to more accurate results, especially with unstructured data. It goes beyond keyword matching by interpreting user intent, making it crucial for advanced AI applications like question-answering systems and chatbots. 

## How it works with LLMs:
- **Text to Vectors (Embeddings):** LLMs create numerical representations (vectors) for words, sentences and documents, where similar meanings have similar vector positions.
- **Contextual Understanding:** It uses Natural Language Processing (NLP) and Machine Learning (ML) to grasp synonyms, intent ("best laptops for students" means powerful graphics, not just "laptops") and contextual relationships.
- **Vector Search:** The system compares the vector of the query with vectors of indexed content, finding the closest matches in meaning.
- **Relevance & Synthesis:** It ranks results based on semantic relevance and can even use the LLM to generate direct, summarized answers from the retrieved information (often via Retrieval-Augmented Generation or RAG).

## **Example:**
- **Query:** "waterproof hiking boots for wide feet"
- **Traditional Search:** Might miss product listings saying "water-resistant trail footwear with spacious toe box".
- **Semantic Search (LLM):** Understands the semantic link and returns relevant options, even with different phrasing, because it grasps the intent. 
