# DevOps & Release

## Recommended Production Stack

- Kubernetes (EKS or equivalent managed cluster)
- PostgreSQL managed service (RDS or equivalent)
- Redis managed service
- Object storage for data lake (S3 or equivalent)
- CI/CD with GitHub Actions and container registry
- Docker for build packaging
- Helm for Kubernetes deployment management

## Release Workflow

1. Build and test in CI.
2. Deploy to staging.
3. Run smoke and regression checks.
4. Approve production rollout.
5. Monitor KPIs and rollback triggers.

## Reliability Practices

- Horizontal autoscaling for API and worker tiers.
- Canary rollout for high-risk changes.
- Error budget and SLO tracking.
