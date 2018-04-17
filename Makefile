LANGAGES = es-py en fr

en:
	cd en && $(MAKE)

es:
	cd es-py && $(MAKE)

fr:
	cd fr && $(MAKE)

.PHONY: en es fr

clean:
		for dir in $(LANGAGES) ; do \
			cd $$dir && $(MAKE) clean ; \
			cd .. ; \
		done
