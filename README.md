# 🚀 Azure Modern Data Lakehouse

## 📌 Overview

This project implements a **Modern Data Lakehouse architecture on Azure** to ingest, process, and transform data into **analytics-ready datasets**.

Data flows from **GitHub → Azure Data Factory → Azure Data Lake → Azure Databricks**, and is orchestrated end-to-end using **Apache Airflow**.

---



## 🔹 Data Source

* **GitHub**

  * Raw CRM and ERP datasets
  * Dataset details available in the `datasets/` folder

---

## 🔹 Data Ingestion

* **Azure Data Factory (ADF)**

  * Loads data from GitHub into **SQL Server**
  * Moves data from SQL Server to **Bronze layer** in Azure Data Lake
  * Uses **incremental load** for efficiency

---

## 🗂️ Data Lake Layers

### 🥉 Bronze (Raw Data)

* Format: Parquet
* Load Type: Incremental
* Transformations: None

### 🥈 Silver (Cleaned Data)

* Format: Delta Tables
* Load Type: Incremental
* Transformations:

  * Data cleaning
  * Standardization
  * Normalization
  * Derived columns

### 🥇 Gold (Business Data)

* Format: Delta Tables
* Load Type: Incremental
* Data Model:

  * Star schema
  * Fact and Dimension tables
  * SCD Type 1

---

## ⚙️ Processing & Orchestration

* **Azure Databricks**

  * Handles all transformations (Bronze → Silver → Gold)
  * Uses Delta Lake and Unity Catalog

* **Apache Airflow**

  * Orchestrates the full pipeline
  * Triggers ADF and Databricks workflows

---

## 🧰 Tools Used

* Azure Data Factory
* Microsoft SQL Server
* Azure Databricks (Delta Lake, Unity Catalog)
* Apache Airflow
* GitHub

---



---

## 🔄 Data Flow

1. GitHub → ADF → SQL Server
2. SQL Server → ADF → Bronze
3. Bronze → Silver (Databricks)
4. Silver → Gold (Star Schema)
5. Airflow orchestrates everything

---

## ⭐ Key Features

* Incremental loading
* Delta Lake support
* Bronze / Silver / Gold layers
* Star schema modeling
* End-to-end automation


