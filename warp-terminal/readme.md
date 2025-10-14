## Warp Git Workflow Demo

#### Goal
Create a reproducible demo you can run from an empty directory to:
- scaffold a tiny Python HTTP app
- containerize it
- create multiple Git branches (including an intentional merge conflict)
- add a CI workflow file
- demonstrate using Warp to manage Git operations with natural language / agentic prompts

#### Prerequisites
- Git installed (git >= 2.20 recommended)
- Warp installed and configured (use `#` to invoke AI suggestions)
- (Optional) Docker to build the image
- (Optional) GitHub CLI (`gh`) to create a remote repo from the command line
- (Optional) Docker Hub or GitHub Packages account to push images from CI

#### Task 1
Create a tiny Python HTTP app. Save as `app.py`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Warp Git Demo!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on :8080")
    server.serve_forever()
```

#### Task 2

Containerize the Python HTTP app. Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the application file
COPY app.py .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
```

**Commands to complete Task 2:**
```bash
# Build the Docker image
docker build -t warp-demo-app .

# Run the container
docker run -p 8080:8080 warp-demo-app

# Test the endpoints
curl http://localhost:8080
curl http://localhost:8080/health

# Run in background (detached mode)
docker run -d -p 8080:8080 --name warp-demo warp-demo-app
