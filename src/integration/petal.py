import matplotlib.pyplot as plt
import seaborn as sns
#'dataset' is the default DataFrame with selected fields
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dataset, x='petal length (cm)', y='sepal length (cm)', hue='species', size='species')
plt.title('Petal Length vs Sepal Length by Species')
plt.show()