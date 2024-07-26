
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

products = {'product_id': [3410, 3510, 3610],
            'description': ['smartphone with good camera', 'laptop with high performance', 'tablet with long battery life']}
product_df = pd.DataFrame(products)

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(product_df['description'])

# Function to recommend similar products
def recommend_similar_products(product_id, num_recommendations):
    product_index = product_df[product_df['product_id'] == product_id].index[0]
    cosine_similarities = cosine_similarity(tfidf_matrix[product_index], tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[:-num_recommendations-1:-1]
    similar_products = product_df['product_id'].iloc[similar_indices]
    return similar_products
