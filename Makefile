
MILKS=$(patsubst %.milk.toml,generated/%.milk, $(wildcard *.milk.toml) $(wildcard saved/*.milk.toml))

all: $(MILKS)

generated/%.milk: %.milk.toml converters/milk2toml.py
	mkdir -p $$(dirname $@)
	cat $< | python3 converters/toml2milk.py > $@

examples/%.milk.toml: examples/%.milk
	cat $< | python3 contervers/milk2toml.py > $@

