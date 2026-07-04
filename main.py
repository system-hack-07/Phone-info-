from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests

app = FastAPI(title="SAMARTH PHONE OSINT")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SAMARTH PHONE OSINT</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {font-family: monospace;}
        button:active {transform: scale(0.95);}
    </style>
</head>
<body class="bg-black text-green-400">
<div class="max-w-xl mx-auto p-8">
    <h1 class="text-6xl text-red-500 text-center">SAMARTH</h1>
    <h2 class="text-4xl text-center mb-8">PHONE OSINT</h2>
    
    <input id="number" class="w-full bg-zinc-900 border border-green-500 p-4 text-xl mb-4" placeholder="Enter number e.g. 919876543210">
    
    <button onclick="fetchData()" 
            class="w-full bg-red-600 py-6 text-2xl hover:bg-red-700">ACQUIRE TARGET INTEL</button>
    
    <div id="result" class="mt-8"></div>
</div>

<script>
async function fetchData() {
    const num = document.getElementById('number').value.trim();
    const res = await fetch('/api/osint?number=' + num);
    const data = await res.json();
    document.getElementById('result').innerHTML = `<pre class="bg-zinc-900 p-6 text-green-300">${JSON.stringify(data, null, 2)}</pre>`;
}
</script>
</body>
</html>"""

@app.get("/")
async def home():
    return HTMLResponse(HTML)

@app.get("/api/osint")
async def osint(number: str):
    try:
        r = requests.get(f"https://sher-osint-india-num-info.vercel.app/api?number={number}", timeout=15)
        return r.json()
    except:
        return {"error": "Failed to fetch intel"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
