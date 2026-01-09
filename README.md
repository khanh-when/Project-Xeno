# Project-Xeno

# **Status: HALTED**

**Stock Market ETL Data Automation Pipeline**

## Notice:
Relational Schema is a working in-progress

____________________
### Note: **Subject To Change**
```text
Automation Pipeline ─────► pipeline.py
                            │
                            ├─ open DB connection
                            ├─ extract
                            ├─ transform
                            ├─ load (cursor, data)
                            ├─ commit
                            └─ close DB connection
```

## Project Layout

![alt text](<misc/Stock Market Project - Frame 1.jpg>)


## **Extraction Layer**

## **Transformation Layer**
```text
Raw Market Data (yFinance API)
                        │
                        ▼
┌──────────────── Extraction ────────────────┐
│     Open | Low | High | Close | Volume     │
└────────────────────────────────────────────┘
                        │
                        ▼
┌────────────── Normalized Time-Series Table ──────────────┐
│   StockID | Date | Open | Low | High | Close | Volume    │
└──────────────────────────────────────────────────────────┘

```

## **Load Layer**



https://crontab.guru/

