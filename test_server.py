from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


PORT = 8000

with ThreadingHTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving HTTP on port {PORT} (http://localhost:{PORT}/) ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n伺服器已停止")