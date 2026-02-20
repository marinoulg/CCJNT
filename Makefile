make main:
	@python method/clean_data.py
	@rm -rf outputs/
	@python main.py

make preprocess:
	@rm -rf data/PCAETs/WIP
	@python preproc/preprocessing_data_ademe_PCAET.py
