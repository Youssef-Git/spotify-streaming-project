# 🎵 Spotify Streaming Data Pipeline

A real-time data engineering pipeline that simulates Spotify streaming events and processes them through a Modern Data Stack (MDS).

## 🏗️ Architecture

Data Simulator → streaming via Kafka → MinIO → Airflow → Databricks Bronze → dbt (Silver & Gold) → Power BI

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Streaming | Apache Kafka |
| Object Storage | MinIO (S3-compatible) |
| Orchestration | Apache Airflow |
| Data Warehouse | Databricks Delta Lake |
| Transformation | dbt |
| Visualisation | Power BI |
| Containerisation | Docker |

## 🥉🥈🥇 Medallion Architecture

**Bronze** → Raw events ingested from MinIO

**Silver** → Cleaned, deduplicated and enriched data

**Gold** → Aggregated analytics-ready tables

## 📁 Repository Structure

<img width="586" height="552" alt="image" src="https://github.com/user-attachments/assets/ca3e6025-2bc1-473d-8af8-d83fc6ac17c7" />


## 📊 Visualization in Power BI

Connected directly to Snowflake Gold layer.

Built interactive visuals:

- 🎵 Top Tracks & Artists
- ⏭️ Skip Rate analysis
- 🌍 Listening habits by country and platform
- 📱 Platform distribution (mobile/desktop/web)

<img width="1484" height="805" alt="image" src="https://github.com/user-attachments/assets/aa57b731-0c0d-4710-8d97-a1aefaf69522" />


