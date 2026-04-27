# Sample App — GitOps CI/CD Demo

![CI](https://github.com/kiran-kumatkar/sample-app/actions/workflows/ci.yaml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/kirankumatkar217/sample-app)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-KIND-blue)

A Python Flask microservice deployed via a fully automated GitOps pipeline using ArgoCD and GitHub Actions.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Application | Python Flask |
| Containerization | Docker |
| CI Pipeline | GitHub Actions |
| Image Registry | DockerHub |
| GitOps / CD | ArgoCD |
| Orchestration | Kubernetes (KIND) |
| Package Manager | Helm |

---

## Architecture

```
Developer pushes code to main
          ↓
GitHub Actions CI triggered
├── Builds Docker image
├── Tags with git SHA  (e.g. v1.0.0-abc1234)
├── Pushes to DockerHub
└── Commits new image tag → gitops-config repo
          ↓
ArgoCD detects new commit in gitops-config
├── Syncs dev namespace      → plain Kubernetes YAML
└── Syncs staging namespace  → Helm chart with value overrides
          ↓
New pods come up, application is live
```

---

## CI/CD Pipeline

Every push to `main` triggers the GitHub Actions workflow:

1. **Build** — Docker image built and tagged with short git SHA
2. **Push** — Image pushed to DockerHub with versioned and `latest` tags
3. **Update** — CI commits updated image tag to [gitops-config](https://github.com/kiran-kumatkar/gitops-config)
4. **Deploy** — ArgoCD detects the config change and deploys automatically

---

## Repository Structure

```
sample-app/
├── app/
│   └── main.py                   # Flask application
├── Dockerfile                    # Container definition
└── .github/
    └── workflows/
        └── ci.yaml               # GitHub Actions CI pipeline
```

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Returns app version and environment info |
| `GET /health` | Health check endpoint for Kubernetes probes |

Sample response from `GET /`:
```json
{
  "message": "GitOps demo app",
  "version": "v1.0.0",
  "environment": "dev"
}
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/kiran-kumatkar/sample-app.git
cd sample-app

# Install dependencies
pip install flask

# Run
python app/main.py

# Test
curl http://localhost:5000/
curl http://localhost:5000/health
```

---

## Docker

```bash
# Build
docker build -t kirankumatkar217/sample-app:v1.0.0 .

# Run
docker run -p 5000:5000 kirankumatkar217/sample-app:v1.0.0

# Pull from DockerHub
docker pull kirankumatkar217/sample-app:latest
```

---

## Related Repository

| Repository | Purpose |
|------------|---------|
| [gitops-config](https://github.com/kiran-kumatkar/gitops-config) | Kubernetes manifests and Helm charts — ArgoCD watches this repo |
