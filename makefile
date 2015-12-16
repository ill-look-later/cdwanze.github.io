project=index


${project}: ${project}.org
	emacs ${project}.org -u "$(id -un)" --batch  -f org-html-export-to-html

${project}.org: FORCE
	python3 make_${project}org.py

FORCE:




