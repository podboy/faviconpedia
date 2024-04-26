MAKEFLAGS += --always-make

all: archive


ico2png:
	python3 scripts/ico2png.py

resize:
	python3 scripts/resize.py

archive: ico2png resize
	git add archive
	git commit --message="archive $$(date '+%F %T')"


install:
	pip3 install --upgrade iconer

uninstall:
	pip3 uninstall -y iconer

reinstall: uninstall install
