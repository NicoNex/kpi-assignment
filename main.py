#!/usr/bin/env python3

import endpoints
import uvicorn

if __name__ == "__main__":
	uvicorn.run(endpoints.app, host="localhost", port=8080)
