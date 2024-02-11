DIR = /usr/local/bin/

install:
	cp cs-adjuster.py $(DIR)/cs-adjuster
	chown root:root $(DIR)/cs-adjuster
	chmod 655 $(DIR)/cs-adjuster
	chmod +x $(DIR)/cs-adjuster
