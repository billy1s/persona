import os
import json
from zipfile import ZipFile
from flaskr import BASE_DIR, db
from sqlalchemy import exc


FILES_TO_PROCCESS = BASE_DIR + "\\api\\inbound_data\\files_to_process"
PROCESSED_FILES = BASE_DIR + "\\api\\inbound_data\\processed_files"

from flaskr.api.models import Person


def UnZip(filepath):
	with ZipFile(filepath) as myzip:
		for file in myzip.filelist:
			if ".json" in file.filename:
				with myzip.open(file) as jsonFile:
					ingestJSONFile(jsonFile)
	file = filepath.split("\\")[-1]
	print(f"Moving file: {file} from {FILES_TO_PROCCESS} to {PROCESSED_FILES}")
	os.replace(filepath, PROCESSED_FILES + "\\" + file)




def ingestJSONFile(jsonFile):
	print("ingestingJSON")
	# split this proccess to run in sepeate thread?
	data = json.load(jsonFile)
	for person in data:
		p = Person(person)
		#print(p.json())
		db.session.add(p)
		# TODO Very slow committing after each row - need a better way to handle duplicates
		try:
			db.session.commit()
		except exc.IntegrityError as e:
			db.session().rollback()
			#TODO add log feature of duplicate row
			print("Duplicate record - Rolling back")


def checkInboundData(dir=FILES_TO_PROCCESS):
	for file in os.listdir(dir):
		if ".zip" in file:
			UnZip(FILES_TO_PROCCESS + "\\" + file)
		else:
			print("No files to process")


