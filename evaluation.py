
from sklearn.metrics import precision_score, recall_score, mean_average_precision_score

true_recommendations = [3410, 6347]
predicted_recommendations = [3410, 3610]

# Calculate evaluation metrics
precision = precision_score(true_recommendations, predicted_recommendations, average='binary')
recall = recall_score(true_recommendations, predicted_recommendations, average='binary')
map_score = mean_average_precision_score([true_recommendations], [predicted_recommendations])
