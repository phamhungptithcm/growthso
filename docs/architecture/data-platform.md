# Data Platform

## Transactional Data Layer

- Primary engine: PostgreSQL.
- Cache layer: Redis.
- Search analytics: Elasticsearch or compatible index.

## Core Entities

- users
- organizations
- domains
- keywords
- rankings
- articles
- reviews
- campaigns

## Analytical Data Layer

Pipeline pattern:

`Event stream -> Data lake -> Warehouse -> BI and model features`

Primary sources:

- crawler data,
- SERP data,
- ads data,
- review data.

Common implementation pattern:

`Kafka -> S3 data lake -> warehouse marts -> analytics and AI features`

## Core Relationships (ERD View)

- users -> organizations -> domains
- domains -> pages -> seo_issues
- domains -> keywords -> rankings
- domains -> articles
- organizations -> ads_accounts
- organizations -> reviews

## Data Quality Expectations

- schema versioning for key tables,
- freshness checks on daily aggregates,
- anomaly alerts for ingestion gaps.
