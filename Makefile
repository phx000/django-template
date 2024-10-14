all:
	py -m venv .venv && .venv\\Scripts\\activate && pip install -r requirements.txt
	vite start project frontend && cd frontend && npm install
	docker-compose up --build -d