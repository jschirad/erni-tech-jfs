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

#### 1 Task
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