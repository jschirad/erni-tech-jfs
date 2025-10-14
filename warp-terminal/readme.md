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

# Stop the container
docker stop warp-demo
```

#### Task 3

Create multiple Git branches with intentional conflicts to demonstrate AI-assisted merge resolution:

**Step 1: Create conflicting feature branches**
```bash
# Create feature-a branch with red theme
git checkout -b feature-a
# Modify app.py: change title to "WARP FEATURE A" and background to red gradient
# Commit changes
git add app.py
git commit -m "feat: implement Feature A with red theme"

# Return to dev branch and create feature-b
git checkout dev
git checkout -b feature-b
# Modify app.py: change title to "WARP FEATURE B" and background to teal gradient
# Commit changes
git add app.py
git commit -m "feat: implement Feature B with teal theme"

# Push both branches
git push origin feature-a
git push origin feature-b
```

**Step 2: Create merge conflicts**
```bash
# Try to merge feature-a into dev
git checkout dev
git merge feature-a  # This should work fine

# Now try to merge feature-b (this will create conflicts!)
git merge feature-b  # Conflict!
```

**Step 3: Resolve conflicts using Warp AI**

When you encounter merge conflicts, use Warp's AI capabilities:

1. **Use Warp AI to understand the conflict:**
   - Type `#` in Warp to activate AI
   - Ask: "Help me understand this git merge conflict"
   - AI will analyze the conflict markers and explain what's happening

2. **Get AI suggestions for resolution:**
   - Ask: "How should I resolve this merge conflict between feature-a and feature-b?"
   - Ask: "Show me the best way to combine these conflicting changes"
   - AI will suggest specific resolution strategies

3. **Use AI to generate resolution commands:**
   - Ask: "Generate the git commands to resolve this conflict"
   - AI will provide step-by-step commands

4. **AI-assisted conflict resolution patterns:**
```bash
# View conflict details
git status
git diff

# Let AI help you edit the conflicted file
# Use Warp AI to suggest which changes to keep, modify, or combine

# After manual resolution, complete the merge
git add app.py
git commit -m "resolve: merge feature-b with intelligent conflict resolution"

# Verify the resolution
git log --oneline --graph
```

**Step 4: Advanced AI-assisted Git operations**
```bash
# Use AI to analyze branch differences
# Ask Warp AI: "Compare the changes between feature-a and feature-b"

# Get AI help for complex merges
# Ask: "What's the best strategy for merging these competing features?"

# Use AI for commit message suggestions
# Ask: "Generate a good commit message for resolving this merge conflict"

# AI-assisted branch cleanup
# Ask: "Help me clean up these feature branches after successful merge"
git branch -d feature-a feature-b
git push origin --delete feature-a feature-b
```

**AI Prompts for Git Workflow Management:**
- "Explain this git conflict and suggest resolution strategies"
- "Help me create a clean merge commit message"
- "What are the best practices for resolving this type of conflict?"
- "Show me how to verify that my merge resolution is correct"
- "Generate commands to test the merged code before finalizing"

This demonstrates how Warp's AI can transform complex git operations into guided, intuitive workflows!
