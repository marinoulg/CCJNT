make main:
	@python method/clean_data.py
	@rm -rf outputs/
	@python main.py
