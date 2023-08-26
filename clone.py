import pywebcopy
from pywebcopy import save_website

kwargs = {'project_name': 'mooooto'} # it will create a folder in desired folder with name 'talalsite'

save_website(
    url='https://shoji-yamamoto-portfolio.vercel.app/',
    project_folder = 'C:\Users\user\Desktop',
    **kwargs
)