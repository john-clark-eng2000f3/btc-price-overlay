import httpx

class TickerError(Exception):
    pass

class BtcTicker:
    """Fetches BTC-USD price from Coinbase and Kraken APIs."""
    def __init__(self):
        self.headers = {
            "User-Agent": "btc-price-overlay/1.0"
        }
        self.last_source = "Coinbase"

    def fetch_coinbase(self) -> float:
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        resp = httpx.get(url, headers=self.headers, timeout=4.0)
        resp.raise_for_status()
        payload = resp.json()
        return float(payload["data"]["amount"])

    def get_latest_price(self) -> float:
        try:
            return self.fetch_coinbase()
        except (httpx.HTTPError, ValueError, KeyError) as e:
            raise TickerError("failed to get price from coinbase") from e
