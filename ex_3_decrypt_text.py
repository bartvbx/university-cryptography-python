from collections import Counter

# Load the file
with open('encrypted.txt', 'r') as file:
    data = file.read()

# Preprocess the data
data = data.replace('\n', ' ')
data = data.replace('\x1c', ' ')
data_wo_spaces = data.replace(' ', '')

# Count words and characters
word_counter = Counter(data.split(' '))
character_counter = Counter(data_wo_spaces)
character_counter_percentage = [(i, str(round(character_counter[i] / len(data_wo_spaces) * 100, 2)) + '%') for i, count in character_counter.most_common()]

# Compare the frequency of occurrence of individual letters in the Polish language
# https://pl.wikipedia.org/wiki/Plik:Polish_letters_frequencies.svg
print(character_counter_percentage)

# Replace most common letters
data = data.replace('m', 'A') # A - 9.90 %
data = data.replace('h', 'E') # E - 8.77 %
data = data.replace('l', 'O') # O - 8.60 %
data = data.replace('a', 'I') # I - 8.21 %

# Compare the frequency of occurrence of individual words in the Polish language
# https://pl.wiktionary.org/wiki/Indeks:Polski_-_Najpopularniejsze_s%C5%82owa_1-1000_wersja_Jerzego_Kazojcia
print(word_counter)

# Replace letters based on most common words
# 'pIE', 'qIE' -> 'SIE', 'NIE'
data = data.replace('p', 'S')
data = data.replace('q', 'N')
# 'i' -> 'W'
data = data.replace('i', 'W')

# Replace letters based on missing letters in individual words
# 'zNIEWINNIONEcO' -> 'UNIEWINNIONEGO'
data = data.replace('z', 'U')
data = data.replace('c', 'G')
# 'NIEWvGOfNIE' -> 'NIEWYGODNIE'
data = data.replace('v', 'Y')
data = data.replace('f', 'D')
# 'NOWEy' -> 'NOWEJ'
data = data.replace('y', 'J')
# 'UWOeNIONEGO' -> 'UWOLNIONEGO'
data = data.replace('e', 'L')
# 'kOWIEDsIAL' -> 'POWIEDZIAL'
data = data.replace('k', 'P')
data = data.replace('s', 'Z')
# 'NIE ZADAWALEd SOtIE JESZrZE nEGO PYnANIA' -> 'NIE ZADAWALEM SOBIE JESZCZE TEGO PYTANIA'
data = data.replace('d', 'M')
data = data.replace('t', 'B')
data = data.replace('r', 'C')
data = data.replace('n', 'T')
# 'NIE POTgZEBUJE PODZIEbOWAN' -> 'NIE POTRZEBUJE PODZIEKOWAN'
data = data.replace('g', 'R')
data = data.replace('b', 'K')
# 'WROCIL DO SWEJ uLASZKI WINA WYCoYLIL JA JEDNYM oAUSTEM' -> 'WROCIL DO SWEJ FLASZKI WINA WYCHYLIL JA JEDNYM HAUSTEM'
data = data.replace('u', 'F')
data = data.replace('o', 'H')
# 'DOwERSKI' -> 'DOVERSKI'
data = data.replace('w', 'V')

# Save file
with open('decrypted.txt', 'w') as file:
    file.write(data)
