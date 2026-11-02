cat << 'EOF' > app.py
import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def hello():
    count = r.incr("hits")
    return f"¹æ¹® È½¼ö: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF