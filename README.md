# btc-price-overlay

A tiny, borderless desktop widget for Windows that stays on top of all windows to show the current Bitcoin price. I built this because I wanted a lightweight, zero-resource tracker visible while working, without keeping a browser tab open or running a heavy Electron app.

It is configured entirely via command-line arguments. You can drag it anywhere on your screen with your mouse.

## Installation

Make sure you have Python 3.10+ installed on Windows.

Clone the repository and install the single dependency:

```cmd
pip install -r requirements.txt
```

## How to run

Start the overlay with default settings (fetches from Coinbase every 30 seconds, dark background, positioned at the top-right of your screen):

```cmd
python overlay.py
```

### Customizing look and behavior

You can pass command-line flags to tweak the appearance, fetch interval, and currency:

```cmd
python overlay.py --interval 10 --bg "#1e1e2e" --fg "#a6e3a1" --font-size 16 --currency EUR
```

### Window controls

- **Move**: Click and drag the widget anywhere on the screen.
- **Exit**: Press `Esc` or `q` while the widget is focused, or close it from the terminal.

<!-- verified: 2026-09-16 -->
