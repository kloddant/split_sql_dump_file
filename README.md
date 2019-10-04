# split_sql_dump_file
Python script to split a single large sql dump file into separate files, one for each CREATE TABLE statement. Writes the files to a new folder that you specify. If no output folder is specified, creates a new folder with the same name as the dump file, in the same directory. Works line-by-line, without writing the file to memory first, so is great for large files.
