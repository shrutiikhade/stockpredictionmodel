# Stock Market Prediction And Forecasting Using Stacked LSTM

This project demonstrates stock market prediction using a stacked LSTM model. The data is sourced from Yahoo Finance.

## Installation

1. Clone the repository and navigate to the project directory:
    ```sh
    git clone https://github.com/yourusername/StockPrediction.git
    cd StockPrediction
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Jupyter notebook:
    ```sh
    jupyter notebook notebooks/hdfc_stock_prediction.ipynb
    ```

2. Follow the steps in the notebook to download data, preprocess it, build and train the model, and make predictions.

## Requirements

- pandas
- numpy
- matplotlib
- scikit-learn
- tensorflow
- yfinance

## Results

The notebook includes various visualizations showing the actual stock prices, the predictions made by the model, and future price predictions.