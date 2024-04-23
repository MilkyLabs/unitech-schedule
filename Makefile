parser_exe := src/main.py

all:
	@echo "Go fuck yourself"

run: $(parser_exe)
	python $(parser_exe)

ifneq ($(OS),Windows_NT) 
setup: $(parser_exe)
	@echo "Make $(parser_exe) executable"
	@chmod +x $(parser_exe)
endif

clear:
	rm -rf __pycache__/
