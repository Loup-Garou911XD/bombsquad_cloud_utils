build:
	python3 setup.py build_ext --inplace

clean:
	git clean -dfx

clean-list:
	git clean -dnx
