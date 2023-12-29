#!/usr/bin/env python3

import uvicorn
from endpoints import app

if __name__ == "__main__":
	uvicorn.run(app, host="localhost", port=8080)
