parser_exe := src/main.py
bot_exe := src/bot.py

all:
	@echo "Go fuck yourself"

run: $(parser_exe)
	python $(parser_exe)

setup: $(parser_exe)
	@echo "Pulling git repository"
	@git pull

ifneq ($(OS),Windows_NT) 
	@echo "Make $(parser_exe) executable"
	@chmod +x $(parser_exe)
endif

	@echo "Install pip packages"
	@pip install -r requirements.txt

clear:
	rm -rf __pycache__/ .cache

include .env

run-bot: $(bot_exe) .env
	@python $(bot_exe)
