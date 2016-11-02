.PHONY: all clean run

all: clean run

clean:
	@rm -f out.py
	@rm -f out-pp.py

run:
	@python3 thera.py
	@cat out.json | jq '.' > out-pp.json
