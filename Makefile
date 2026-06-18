build:
	pyinstaller main.py -F -n pyref
	pyinstaller make_ref_page.py -F -n pyref_m
	echo Done.
