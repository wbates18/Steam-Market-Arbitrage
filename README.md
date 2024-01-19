# Steam Market Arbitrage Bot

## Description

Script designed to scrape cost of all csgo skins from market and calculate if in game CSGO functionality would be profitable. In CSGO, you can convert 10 skins of one rarity, to 1 of the next highest. This script calculates if that transaction could be profitable (after fees). Uses vpn switching to get around API limits.

## Usage

Set API keys for currency conversion in each of the main files, set up discord API in discordbot.py, and use:
```
chmod +x Tradeup.sh
./Tradeup.sh
```
Make sure that a vpn is set up on the device and it is CLI manageable, with it configured in each main file correctly.
