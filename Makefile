
MILKS=$(patsubst %.milk.toml,generated/%.milk, $(wildcard *.milk.toml) $(wildcard saved/*.milk.toml))
TOMLS=$(patsubst %.milk,%.milk.toml, $(wildcard examples/*.milk))

all: $(MILKS) $(TOMLS)

clean: 
	git clean -fdX

generated/%.milk: %.milk.toml converters/milk2toml.py
	mkdir -p $$(dirname $@)
	cat $< | python3 converters/toml2milk.py > $@

examples/%.milk.toml: examples/%.milk
	cat "$<" | python3 converters/milk2toml.py > "$@"

