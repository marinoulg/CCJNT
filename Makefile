make preprocess:
	@rm -rf data/PCAETs/WIP
	@python preproc/preprocessing_data_ademe_PCAET.py

make install:
	@pip install -r requirements.txt
	@pip install -e .

make main:
# 	@make install
	@make preprocess
# 	@python method/clean_data.py
	@rm -rf outputs/
	@python main.py
