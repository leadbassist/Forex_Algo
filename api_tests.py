from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

from models.candle_timing import CandleTiming

if __name__ == "__main__":
    api = OandaApi()

    # to load instruments from "data"folder
    instrumentCollection.LoadInstruments("./data")

    # # open trade
    # trade_id = api.place_trade("EUR_USD", 100, 1)
    # print("opened: ", trade_id)

    # # wait 10 seconds
    # time.sleep(10)

    # # close trade
    # print(f"Closing {trade_id}", api.close_trade(trade_id))

    # # get a specific open trade
    # print(api.get_open_trade(120))

    # # show all open trades
    # [print(x) for x in api.get_open_trades()]

    # # close all open trades
    # [api.close_trade(x.id) for x in api.get_open_trades()]

    # # get the last completed candle
    # print(api.last_complete_candle("EUR_USD", granularity="M5"))

    # # get an instance of the latest candle time
    # dd = api.last_complete_candle("EUR_USD", granularity="M5")
    # print(CandleTiming(dd))

    # print live prices
    print(api.get_prices(["GBP_JPY", "AUD_NZD"]))
