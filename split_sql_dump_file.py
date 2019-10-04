import sys, re, os

if sys.version_info[0] < 3:
	raise Exception("""Must be using Python 3.  Try running "C:\\Program Files (x86)\\Python37-32\\python.exe" split_sql_dump_file.py""")

sqldump_path = input("Enter the path to the sql dump file: ") or os.path.expanduser("~") + "\\Desktop\\popularwoodworking.sql"

if not os.path.exists(sqldump_path):
	raise Exception("Invalid sql dump path.  {sqldump_path} does not exist.".format(sqldump_path=sqldump_path))

output_folder_path = input("Enter the path to the output folder: ") or sqldump_path.rstrip('.sql')

if not os.path.exists(output_folder_path):
	os.makedirs(output_folder_path)

table_name = None
output_file_path = None
smallfile = None

with open(sqldump_path, 'rb') as bigfile:
	for line_number, line in enumerate(bigfile):
		line_string = line.decode("utf-8")
		if 'CREATE TABLE' in line_string.upper():
			match = re.match(r"^CREATE TABLE (?:IF NOT EXISTS )?`(?P<table>\w+)` \($", line_string)
			if match:
				table_name = match.group('table')
				print(table_name)
				output_file_path = "{output_folder_path}/{table_name}.sql".format(output_folder_path=output_folder_path.rstrip('/'), table_name=table_name)
				if smallfile:
					smallfile.close()
				smallfile = open(output_file_path, 'wb')
		if not table_name:
			continue
		smallfile.write(line)
	smallfile.close()
