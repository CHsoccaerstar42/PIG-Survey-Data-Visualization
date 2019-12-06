from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

responses = [7, 4, 6, 5, 9, 5, 7, 5, 6, 7, 9, 7, 6, 7,
             5, 9, 7, 1, 5, 9, 3, 8, 2, 8, 7, 'none',
             8, 8, 5, 'none', 'none', 5, 1, 4, 5, 6,
             9, 6, 7, 1, 6, 4, 8, 'none', 7, 9, 5, 6, 'none'#10
             , 5, 1, 5, 6, 6, 7, 7, 8, 7, 6, 7, 6, 5, 4, 7, 'none'#5
             , 8, 6, 8, 'none', 3, 5, 4, 'none', 6, 4, 7, 7, 5]
#colors = ['#f8e9a1', '#f76c6c', '#a8d0e6', '#374785', '#24305e',
#          '#a64ac9', '#fccd04', '#ffb48f', '#f5e6cc', '#17e9e0']
final = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in responses:
    if i != 'none':
        final[i - 1] += 1

labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

plt.pie(final, labels=labels, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
plt.title('Standardized Test Accuracy')
plt.show()
