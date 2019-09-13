import subprocess
list_of_packages =['pyyaml'
				,'regex'
				,'requests'
				,'urllib3'
				,'BeautifulSoup4'
				,'nltk'
				,'pandas'
				,'sqlalchemy']
				
for i in list_of_packages:
	try:
		import i
	except ModuleNotFoundError:
		subprocess.run(['pip','install',i])
