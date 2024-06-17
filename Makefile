
MILKS=$(patsubst %.milk.toml,generated/%.milk, $(wildcard *.milk.toml))

all: $(MILKS)

generated/%.milk: %.milk.toml converters/milk2toml.py
	cat $< | python3 converters/toml2milk.py --decode > $@

