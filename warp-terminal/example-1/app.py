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

        # Serve HTML page with styling
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Warp Git Demo</title>
            <style>
                body {
                    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
                    margin: 0;
                    padding: 0;
                    font-family: 'Arial', sans-serif;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }
                h1 {
                    font-size: 4rem;
                    font-weight: bold;
                    margin-bottom: 1rem;
                    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
                    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                }
                p {
                    font-size: 1.5rem;
                    margin-bottom: 0.5rem;
                }
                .demo-info {
                    font-size: 1.2rem;
                    opacity: 0.9;
                }
                .health-link {
                    display: inline-block;
                    margin-top: 2rem;
                    padding: 10px 20px;
                    background: rgba(255, 255, 255, 0.2);
                    border: 2px solid rgba(255, 255, 255, 0.3);
                    border-radius: 25px;
                    color: white;
                    text-decoration: none;
                    transition: all 0.3s ease;
                }
                .health-link:hover {
                    background: rgba(255, 255, 255, 0.3);
                    transform: translateY(-2px);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>WARP FEATURE A</h1>
                <p>Hello from Feature A - Red Theme!</p>
                <p class="demo-info">Running in Docker Container 🐳 | Feature A Branch</p>
                <a href="/health" class="health-link">Check Health Status</a>
            </div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Listening on :8080")
    server.serve_forever()
