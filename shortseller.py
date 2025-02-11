import streamlit as st
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# Inicializar la aplicación Streamlit
st.title("GUILLERMO - ShortSeller")

# Parámetros de actualización
refresh_interval = 5  # Intervalo de actualización en segundos

# Agregar el autorefresco
count = st_autorefresh(interval=refresh_interval * 1000, key="autorefresh")

# Entrada de datos
ticker = st.text_input("Enter Ticker Symbol", value="NUKK")

# Lista de tickers
if 'tickers' not in st.session_state:
    st.session_state['tickers'] = []

def add_ticker():
    if ticker and ticker.upper() not in st.session_state['tickers']:
        stock = yf.Ticker(ticker.upper())
        try:
            # Verificar si el ticker existe obteniendo datos históricos
            stock.history(period='1d')
            st.session_state['tickers'].append(ticker.upper())
        except:
            st.error(f"No data found for ticker: {ticker.upper()}")

def remove_ticker():
    if ticker and ticker.upper() in st.session_state['tickers']:
        st.session_state['tickers'].remove(ticker.upper())

# Botones para agregar y eliminar tickers
st.button("Add Ticker", on_click=add_ticker)
st.button("Remove Ticker", on_click=remove_ticker)

# Mostrar la lista de tickers
#st.write("Tickers:", st.session_state['tickers'])

# Mostrar el tiempo de refresco restante
time_until_next_update = refresh_interval - (count % refresh_interval)
st.write(f"Refresh Time: {time_until_next_update} Seconds")

# Actualizar la información de los tickers
if st.session_state['tickers']:
    num_columns = 3  # Número de columnas en la cuadrícula
    columns = st.columns(num_columns)
    index = 0
    
    for t in st.session_state['tickers']:
        stock = yf.Ticker(t)
        hist = stock.history(period='1d')
        current_price = stock.info.get('currentPrice', 'N/A')
        
        if hist.empty:
            with columns[index % num_columns]:
                st.write(f"No data found for ticker: {t}")
        else:
            open_price = hist['Open'].iloc[0]
            price_change_pct = ((current_price - open_price) / open_price) * 100
            price_5 = open_price * 1.05
            price_10 = open_price * 1.10
            price_15 = open_price * 1.15
            price_20 = open_price * 1.20
            price_25 = open_price * 1.25
            price_30 = open_price * 1.30
            stop_loss = open_price * 1.40

            with columns[index % num_columns]:
                st.subheader(f"Ticker: {t}")
                st.markdown(
                    f"<p style='color: #f4d03f; font-size: 20px;'>Current Price: ${current_price:.2f} ({price_change_pct:.2f}%)</p>",
                    unsafe_allow_html=True
                )
                st.markdown(f"<p style='color: #5dade2; font-size: 20px;'>Open Price: ${open_price:.2f}</p>", unsafe_allow_html=True)
                st.write(f"at 5% : ${price_5:.2f}")
                st.write(f"at 10% : ${price_10:.2f}")
                st.write(f"at 15% : ${price_15:.2f}")
                st.write(f"at 20% : ${price_20:.2f}")
                st.write(f"at 25% : ${price_25:.2f}")
                st.write(f"at 30% : ${price_30:.2f}")
                st.markdown(f"<p style='color: #ec7063; font-size: 24px;'>40% StopLost : ${stop_loss:.2f}</p>", unsafe_allow_html=True)

        index += 1
