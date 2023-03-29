from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from db.db import DataDB

# from simulation.ema_macd import run_ema_macd
from simulation.ema_macd_mp import run_ema_macd
from dateutil import parser
from infrastructure.collect_data import run_collection
from stream_example.streamer import run_streamer


def db_tests():
    d = DataDB()

    # d.add_one(DataDB.SAMPLE_COLL, dict(age=18, name="pinpin", address="the shire"))

    # print(d.query_single(DataDB.SAMPLE_COLL, age=18))
    # print(d.query_all(DataDB.SAMPLE_COLL, age=18, eyes="brown"))
    print(d.query_distinct(DataDB.SAMPLE_COLL, "age"))

    # data = [
    #     dict(age=18, name="frodo", eyes="blue"),
    #     dict(age=18, name="sam", eyes="brown"),
    #     dict(age=68, name="aragorn", eyes="blue"),
    #     dict(age=247, name="gandalf", eyes="gray"),
    #     dict(age=1011, name="sauron", eyes="fire"),
    # ]
    # d.add_many(DataDB.SAMPLE_COLL, data)


if __name__ == "__main__":
    api = OandaApi()

    # to load instruments from "data"folder
    # instrumentCollection.LoadInstruments("./data")

    # instrumentCollection.CreateDB(api.get_account_instruments())

    instrumentCollection.LoadInstrumentsDB()
    print(instrumentCollection.instruments_dict)

    # to get instruments from Oanda API
    # run_collection(instrumentCollection, api)

    # run_ma_sim()
    # run_ema_macd(instrumentCollection)
    # run_ema_macd(instrumentCollection)

    # run_streamer()

    # d = DataDB()
    # d.test_connection()

    # db_tests()
