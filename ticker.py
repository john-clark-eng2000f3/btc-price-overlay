import httpx
from typing import Tuple

class TickerError(Exception):
    pass

class BtcTicker:
    """Fetches BTC-USD price from Coinbase and Kraken APIs."""
    def __init__(self):
        self.headers = {
            "User-Agent": "btc-price-overlay/1.0"
        }
        self.last_source = "None"

    def fetch_coinbase(self) -> float:
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        resp = httpx.get(url, headers=self.headers, timeout=4.0)
        resp.raise_for_status()
        payload = resp.json()
        return float(payload["data"]["amount"])

    def _fetch_kraken(self) -> float:
        # kraken payload structure is slightly more nested
        url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
        resp = httpx.get(url, headers=self.headers, timeout=5.0)
        resp.raise_for_status()
        payload = resp.json()
        
        if payload.get("error"):
            # TODO: kraken api sometimes returns a list of errors, we should check it specifically if we start getting empty results
            raise ValueError(f"Kraken API error: {payload['error']}")
            
        ticker_data = payload["result"]["XXBTZUSD"]
        return float(ticker_data["c"][0])

    def get_latest_price(self) -> Tuple[float, str]:
        # Try Coinbase first, fall back to Kraken if API is ratelimited or down
        try:
            price = self.fetch_coinbase()
            self.last_source = "Coinbase"
            # print(f"dbg: coinbase fetched {price}")
            return price, self.last_source
        except (httpx.HTTPError, ValueError, KeyError):
            pass

        try:
            price = self._fetch_kraken()
            self.last_source = "Kraken"
            return price, self.last_source
        except (httpx.HTTPError, ValueError, KeyError) as e:
            raise TickerError("both price sources failed") from e
