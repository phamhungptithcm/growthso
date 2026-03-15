# Kubernetes Production

## Cluster Components

- API services
- Crawler workers
- Ranking workers
- AI processing workers

## Infrastructure Baseline

- Managed Kubernetes (AWS EKS or equivalent)
- Horizontal Pod Autoscaling
- Service mesh for traffic control and observability

## Deployment Guidelines

- Use Helm charts for repeatable releases.
- Separate namespaces by environment and service domain.
- Roll out worker pools independently from API services to reduce risk.
