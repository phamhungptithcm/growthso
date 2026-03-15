# System Overview

## High-Level Architecture

```mermaid
flowchart LR
    A[Web and Mobile Clients] --> B[API Gateway]
    B --> C[Core Microservices]
    C --> D[(PostgreSQL)]
    C --> E[(Redis)]
    C --> F[(Search and Analytics)]
    C --> G[(Event Stream)]
    G --> H[Workers and AI Pipelines]
    H --> I[(Data Lake and Warehouse)]
```

## Design Goals

- Reliable APIs for daily growth operations.
- Scalable asynchronous processing for crawlers and AI workloads.
- Clear boundaries between transactional and analytical systems.
