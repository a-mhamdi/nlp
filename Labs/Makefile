DIR := $(wildcard *.typ)
EXCLUDE := Class.typ Timeline.typ Preamble.typ

FILES := $(filter-out $(EXCLUDE), $(DIR))

typst := ${HOME}/apps/bin/typst 

task: 
	$(foreach file,$(FILES),${typst} compile --root ../ $(file);)

