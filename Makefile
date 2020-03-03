### Housekeeping ###################################

clean:
	@echo "Cleaning directory..." 
	rm -rf venv
	@echo "...Done."

PY?=python3
venv:
	@echo "Creating venv..."
	$(PY) -m venv venv
	@echo "...Done."

install: venv
	@echo "Installing Paint..."
	@( \
		source venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
	)
	@echo "...Done."

### Running The API #################################

runserver:
	@echo "Running local server..."
	@manage.py runserver