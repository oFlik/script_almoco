from dotenv import load_dotenv
import sys
import os

#load_dotenv(override=True)

extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS
load_dotenv(override=True, dotenv_path=os.path.join(extDataDir, '.env'))

NAME = os.getenv("NAME")
FORM_LINK = os.getenv("FORM_LINK")
WAIT_TIME = 1

divisions = [
    "Desenvolvimento",
    "Sistemas",
    "Helpdesk",
    "Infraestrutura",
    "Processamento",
]

option_paths = {
    "namefield": os.getenv("NAMEFIELD"),
    "company_checkbox": os.getenv("COMPANY_CHECKBOX"),
    "department_checkbox": os.getenv("DEPARTMENT_CHECKBOX"),
    "quantity_field": os.getenv("QUANTITY_FIELD"),
    "divisions_dropbox": os.getenv("DVISIONS_DROPBOX"),
    "submit": os.getenv("SUBMIT"),
}
