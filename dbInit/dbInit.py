import os,glob, views_model

folder_path = r'C:\Users\aleks\Downloads\TestEx'
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
  with open(filename, 'r', encoding='utf8') as f:
    text = f.read()
    print (filename)
    print (len(text))
