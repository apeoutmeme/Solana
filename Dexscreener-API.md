# DEXSCREENER API
https://docs.dexscreener.com/api/reference

## ENDPOINTS
Get the latest token profiles (rate-limit 60 requests per minute)
`GET https://api.dexscreener.com/token-profiles/latest/v1`

Get the latest boosted tokens (rate-limit 60 requests per minute)
`GET https://api.dexscreener.com/token-boosts/latest/v1`

`GET https://api.dexscreener.com/latest/dex/tokens/{tokenAddresses}
{
  "schemaVersion": "text",
  "pairs": [
    {
      "chainId": "text",
      "dexId": "text",
      "url": "https://example.com",
      "pairAddress": "text",
      "labels": [
        "text"
      ],
      "baseToken": {
        "address": "text",
        "name": "text",
        "symbol": "text"
      },
      "quoteToken": {
        "address": "text",
        "name": "text",
        "symbol": "text"
      },
      "priceNative": "text",
      "priceUsd": "text",
      "liquidity": {
        "usd": 0,
        "base": 0,
        "quote": 0
      },
      "fdv": 0,
      "marketCap": 0,
      "info": {
        "imageUrl": "https://example.com",
        "websites": [
          {
            "url": "https://example.com"
          }
        ],
        "socials": [
          {
            "platform": "text",
            "handle": "text"
          }
        ]
      },
      "boosts": {}
    }
  ]
}`


# Other Endpoints: 
## Get one or multiple pairs by token address (rate-limit 300 requests per minute)

```GET https://api.dexscreener.com/latest/dex/tokens/{tokenAddresses}```

Search for pairs matching query (rate-limit 300 requests per minute)
`GET https://api.dexscreener.com/latest/dex/search
`
Get one or multiple pairs by chain and pair address (rate-limit 300 requests per minute)
`GET https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}
`
Check orders paid for of token (rate-limit 60 requests per minute)
`GET https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}`

Get the tokens with most active boosts (rate-limit 60 requests per minute)
`GET https://api.dexscreener.com/token-boosts/top/v1`


## EXTRA INFORMATION AND FILTERS: 
### Dexscreener Filters: 
Add some special filters:
▪ Min liquidity: $15,000
▪ Min market cap: $700,000
▪ Max pair age: 48 hours
▪ 24 txns: 1000
▪ 24h volume: 1,000,000

### Finding Top Traders 
https://x.com/0xPepesso/status/1841554579596460148










