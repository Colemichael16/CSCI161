#Cole McLean CSCI 161 MWF Class Tur Lab
import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('aapl.csv')
print(aapl.head())
aapl['Date'] = pd.to_datetime(aapl['Date'])

plt.figure(figsize=[5,6])
plt.plot(aapl['Date'], aapl['Close'], label='AAPL Price',)
plt.grid(linestyle = '-')
plt.title('AAPL Stock History')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.savefig('aapl.png')