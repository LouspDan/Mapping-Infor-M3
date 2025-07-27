init:
	pip install -r requirements.txt

extract:
	python src/extract/extract_ap.py

test:
	pytest -q

all: init extract test
	@echo "✅ Pipeline complet exécuté avec succès !"
