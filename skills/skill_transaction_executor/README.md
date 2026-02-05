text### skills/skill_transaction_executor/README.md

````markdown
# Skill: Transaction Executor

## Description

Executes on-chain tx via Coinbase AgentKit.

## Input Contract

```python
class TxInput(BaseModel):
    to_address: str
    amount_usdc: float
```
````

Output Contract
Pythonclass TxOutput(BaseModel):
tx_hash: str
success: bool

```
# Skill: Transaction Executor

Purpose: execute transactions and report status.
```
