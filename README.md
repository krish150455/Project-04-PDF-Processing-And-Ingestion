# Project 04 - PDF Processing & Document Ingestion System

## Overview

This project is the fourth step in my Retrieval-Augmented Generation (RAG) learning journey.

In previous projects, I worked with manually-created text files. However, real-world RAG systems rarely operate on simple text files. Most enterprise knowledge bases consist of PDFs such as:

* Research papers
* Technical documentation
* Reports
* Books
* Policies
* Annual reports

Before retrieval can happen, these documents must be processed and converted into a structured format that can later be chunked, embedded, and stored.

This process is known as **Document Ingestion**.

---

## Understanding RAG Pipelines

A real RAG system typically consists of two pipelines.

### Offline Pipeline

Responsible for preparing documents.

```text
PDF
↓
Text Extraction
↓
Metadata Extraction
↓
Chunking
↓
Embeddings
↓
Vector Database Storage
```

### Online Pipeline

Responsible for answering user queries.

```text
User Query
↓
Query Embedding
↓
Retrieval
↓
LLM
↓
Generated Answer
```

This project focuses entirely on the offline pipeline.

---


## Technologies Used

* Python
* PyPDF2

---

## Architecture

```text
PDF
↓
PDF Reader
↓
Page Extraction
↓
Metadata Extraction
↓
Quality Analysis
↓
Structured Document Records
```

---

## Document Structure

Each page is converted into a structured record.

Example:

```python
{
    "page": 1,
    "text": "...",
    "source": "pages.pdf",
    "author": "...",
    "title": "...",
    "status": "good"
}
```

This structure will later be used for:

* Chunking
* Embeddings
* Retrieval
* Source Attribution

---

## Features Implemented

### 1. PDF Loading

PDF files are loaded using:

```python
PdfReader()
```

The ingestion system can determine:

* Total pages
* Page contents
* Document metadata

---

### 2. Text Extraction

Text is extracted page-by-page.

```python
page.extract_text()
```

This preserves page boundaries which are important for future retrieval systems.

---

### 3. Metadata Extraction

Document metadata is captured automatically.

Extracted fields include:

* Author
* Creator
* Producer
* Subject
* Title

Metadata becomes useful later for:

```text
Metadata Filtering
Source Tracking
Document Attribution
```

which are common features in production RAG systems.

---

### 4. Quality Assessment

Each page is evaluated for extraction quality.

Rules:

```text
No Text
↓
empty

Very Short Text
↓
suspicious

Normal Text
↓
good
```

This helps identify:

* Blank pages
* Corrupted pages
* Failed extraction attempts

before chunking and embedding.

---

## Reusable Ingestion Pipeline

The project implements a modular ingestion workflow.

### Step 1

```python
load_pdf()
```

Loads a PDF document.

### Step 2

```python
extract_pages()
```

Extracts page text and page information.

### Step 3

```python
extract_metadata_quality()
```

Adds metadata and quality indicators.

### Step 4

```python
ingest_pdf()
```

Combines all steps into a complete ingestion pipeline.

---

## Output Example

```python
[
    {
        "page": 1,
        "source": "report.pdf",
        "text": "...",
        "author": "John Doe",
        "title": "Annual Report",
        "status": "good"
    },
    ...
]
```

This structured representation is significantly more useful than raw PDF text.


---

## Key Takeaway

Retrieval quality depends heavily on document quality.

Before building embeddings, vector databases, or RAG systems, documents must first be ingested and structured correctly.

This project introduced the offline side of RAG systems by building a reusable PDF ingestion pipeline capable of:

* Extracting text
* Preserving page information
* Capturing metadata
* Performing quality checks

and preparing documents for chunking and retrieval in later projects.
