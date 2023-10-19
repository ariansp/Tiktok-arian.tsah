import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Tiktok\\Mahfud MD Wapres\\sentiment Mahfud MD Wapres - mahfud wapres.csv")

df.head()

# Calculate value counts for the 'Category' column
value_counts = df['hasil'].value_counts()

# Create a bar chart from the value counts
plt.bar(value_counts.index, value_counts.values)

for i, v in enumerate(value_counts.values):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
    
plt.xlabel('sentiment')
plt.ylabel('jumlah')
plt.title("Analisis sentiment postingan PDI Perjuangan")

plt.show()


#Wordcloud
from wordcloud import WordCloud
text = ' '.join(str(item) for item in df['Sentiment'] if isinstance(item, str))

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels
plt.title('Word Cloud from DataFrame')
plt.show()
