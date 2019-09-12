list_of_packages =['yaml','argparse','datetime','shutil','csv','logging','regex','requests','urllib3','BeautifulSoup4','nltk','urllib','pandas','hashlib','sqlalchemy']
import subprocess
for i in list_of_packages:
	try:
		import i
	except ModuleNotFoundError:
		subprocess.run(['pip','install',i])

import logging
logging.basicConfig(level=logging.INFO)
import datetime
import shutil
logger= logging.getLogger(__name__)
# to add more news_sites_uids, you will need to edit the file config.yaml 
# config.yaml is inside the folder Extract
news_sites_uids= ['eluniversal','elpais','panorama']


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    
    for news_site_uid in news_sites_uids:
        subprocess.run(['python','main.py',news_site_uid], cwd='./Extract')
    for news_site_uid in news_sites_uids:
        shutil.move("Extract/{a}_{b}_articles.csv".format(a = news_site_uid,b=now),"Transform/{a}_{b}_articles.csv".format(a = news_site_uid, b = now))


def _transform():
    logger.info('Starting transform process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{a}_{b}_articles.csv'.format(a= news_site_uid,b=now)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python','main.py', dirty_data_filename], cwd = './Transform')
       # shutil.rmtree('Transform/{}'.format(dirty_data_filename))
        shutil.move('Transform/{}'.format(clean_data_filename),'Load/{}'.format(clean_data_filename))
    
    
def _load():
    logger.info('Starting load process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    for news_site_uid in news_sites_uids:
        clean_data_filename = 'clean_{a}_{b}_articles.csv'.format(a=news_site_uid,b=now)
        subprocess.run(['python','main.py', clean_data_filename], cwd = './Load')
       # subprocess.run(['rm',clean_data_filename], cwd = './Load')

    
if __name__ == '__main__':
    main()

