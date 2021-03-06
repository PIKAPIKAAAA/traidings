import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("JNJ.csv")
    print(df)
    df['Close'].plot()
    plt.savefig('graphs/aapl.png')

def get_max_close(symbol):
    df = pd.read_csv(f"{symbol}.csv")
    return df['Close'].max()

def main():
    print('Max Close:')
    for symbol in ['JNJ']:
        print(symbol + ":", get_max_close(symbol))

if __name__ == "__main__":
    main()
