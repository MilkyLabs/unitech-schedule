parser_exe := src/main.py
bot_exe := src/bot.py

help:
	@echo "Unitech Timetable Bot Makefile"
	@echo ""
	@echo "\`make setup\`	-	setup this repository for work"
	@echo "\`make run-bot\`	-	run telegram bot"
	@echo "\`make clear\`	-	deletes all cache files"

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
