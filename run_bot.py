from bot.bot import Bot
from infrastructure.instrument_collection import instrumentCollection


if __name__ == "__main__":
    # to load instruments from mongo DB
    instrumentCollection.LoadInstrumentsDB()
    b = Bot()
    b.run()
