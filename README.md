### Note on Binance KYC

Due to recent Binance policy changes requiring mandatory identity verification,
this project uses a mocked Binance Futures Testnet client by default.

The mock client simulates real Binance Futures API responses and preserves:
- order placement logic
- request/response structure
- logging behavior
- error handling

This approach is commonly used in technical assessments to ensure reproducibility.
