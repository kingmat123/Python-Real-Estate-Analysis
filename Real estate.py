import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

#Wczytanie pliku z danymi
data = pd.read_excel('full_data.xlsx', index_col = 0)
#Usunięcie brakujących danych
data.dropna(inplace = True)

#Wyświetlenie statystyk dla wszystkich cech
print(data.describe())
#Wyświetlenie statystyki częstości dla cechy "piętro"
print(data['pietro'].value_counts())

#Wyodrębneinie pierwszych pięciu najczęściej występujących pięter i zwizualizowanie na wykresie
first_five = data['pietro'].value_counts().head(5)
plt.bar(first_five.index, first_five.values,  color = 'green')
plt.title('Top 5 najczęściej występujących pięter')
plt.xlabel('Piętro')
plt.ylabel('Liczba wystąpień')
plt.show()

#Wykres rozrzutu dla cechy "cena" oraz "powierzchnia"
plt.scatter(data['powierzchnia'], data['cena'] / 1000, color = 'purple', alpha = 0.7)
plt.title('Zależność między ceną a powierzchnią')
plt.xlabel('Powierzchnia [m²]')
plt.ylabel('Cena [tys PLN]')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Obliczenie korelacji Spearmana
spearman_corr = data.corr(method='spearman')

# Wyświetlenie macierzy korelacji
print(spearman_corr)

# Wizualizacja macierzy korelacji w formie mapy cieplnej
plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Macierz korelacji Spearmana')
plt.show()

