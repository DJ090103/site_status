.PHONY: run kill clean

PORT ?= 8080
SECRETS_FILE=secrets.json

run:
	@echo "🔵 Checking if port $(PORT) is already in use..."
	@if lsof -i :$(PORT); then \
		echo "🛑 Port $(PORT) is busy. Killing process..."; \
		fuser -k $(PORT)/tcp; \
	fi
	@echo "🚀 Starting FastAPI server on port $(PORT)..."
	@SECRETS_FILE=$(SECRETS_FILE) python3 server.py

kill:
	@echo "🛑 Killing process on port $(PORT)..."
	@fuser -k $(PORT)/tcp || echo "✅ No process found on port $(PORT)."

test:
	pytest