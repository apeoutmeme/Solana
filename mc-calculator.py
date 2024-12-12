import pandas as pd
from datetime import datetime
import numpy as np

class MarketCapEstimator:
    def __init__(self):
        self.LAMPORTS_PER_SOL = 1000000000  # Solana constant
        
    def estimate_entry_market_cap(self, transaction_data, token_data):
        """
        Estimates the market cap at entry point using transaction data and token information.
        
        Parameters:
        transaction_data: dict
            - amount_sol: float (amount of SOL paid)
            - timestamp: int (transaction timestamp)
            - token_amount: float (tokens received)
        token_data: dict
            - total_supply: float (total token supply)
            - initial_timestamp: int (token creation timestamp)
        
        Returns:
        dict: Estimated market cap and confidence score
        """
        try:
            # Calculate price per token in SOL
            price_per_token = transaction_data['amount_sol'] / transaction_data['token_amount']
            
            # Calculate implied market cap at entry
            implied_market_cap = price_per_token * token_data['total_supply'] * self.LAMPORTS_PER_SOL
            
            # Calculate time since token creation
            time_since_creation = transaction_data['timestamp'] - token_data['initial_timestamp']
            
            # Adjust for potential liquidity differences based on time since creation
            # Earlier transactions typically have lower liquidity and may not reflect true market cap
            time_factor = min(1.0, time_since_creation / (24 * 3600))  # Normalize to 1 day
            
            # Apply liquidity adjustment
            adjusted_market_cap = implied_market_cap * (1 + (1 - time_factor))
            
            # Calculate confidence score based on various factors
            confidence_score = self._calculate_confidence_score(
                time_factor,
                transaction_data['amount_sol'],
                transaction_data['token_amount'],
                token_data['total_supply']
            )
            
            return {
                'estimated_entry_market_cap': adjusted_market_cap,
                'raw_market_cap': implied_market_cap,
                'confidence_score': confidence_score,
                'time_factor': time_factor,
                'price_per_token_sol': price_per_token
            }
            
        except Exception as e:
            print(f"Error calculating market cap: {str(e)}")
            return None
    
    def _calculate_confidence_score(self, time_factor, amount_sol, token_amount, total_supply):
        """
        Calculate a confidence score (0-1) for the market cap estimation.
        """
        # Base confidence starts at 0.5
        confidence = 0.5
        
        # Adjust based on time factor (newer tokens have lower confidence)
        confidence += time_factor * 0.2
        
        # Adjust based on transaction size relative to total supply
        supply_factor = min(1.0, (token_amount / total_supply) * 100)
        confidence += supply_factor * 0.2
        
        # Adjust based on SOL amount (larger transactions generally more reliable)
        sol_factor = min(1.0, amount_sol / 10)  # Normalize to 10 SOL
        confidence += sol_factor * 0.1
        
        return min(1.0, max(0.0, confidence))

# Example usage
def demonstrate_estimator():
    estimator = MarketCapEstimator()
    
    # Example transaction data
    transaction = {
        'amount_sol': 0.5,  # 0.5 SOL spent
        'timestamp': int(datetime.now().timestamp()),
        'token_amount': 1000000  # 1M tokens received
    }
    
    # Example token data
    token = {
        'total_supply': 1000000000,  # 1B total supply
        'initial_timestamp': int(datetime.now().timestamp()) - 3600  # Created 1 hour ago
    }
    
    result = estimator.estimate_entry_market_cap(transaction, token)
    
    if result:
        print("\nMarket Cap Estimation Results:")
        print(f"Estimated Entry Market Cap: {result['estimated_entry_market_cap'] / 1000000:.2f}M SOL")
        print(f"Raw Market Cap: {result['raw_market_cap'] / 1000000:.2f}M SOL")
        print(f"Confidence Score: {result['confidence_score']:.2%}")
        print(f"Time Factor: {result['time_factor']:.2f}")
        print(f"Price per Token: {result['price_per_token_sol']:.8f} SOL")

if __name__ == "__main__":
    demonstrate_estimator()
