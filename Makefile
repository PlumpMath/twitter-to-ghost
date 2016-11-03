.PHONY: all clean run

all: clean run

clean:
	@rm -f out.py
	@rm -f out-pp.py

run:
	@python thera.py
