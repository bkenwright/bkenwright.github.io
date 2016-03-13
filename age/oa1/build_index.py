

#<table border="7" cellpadding="10">
#<tr>
#<td><a href="http://www.google.com/">Google.com</a></td>
#<td><a href="http://www.yahoo.com/">Yahoo!</a></td>
#</tr>
#<tr>
#<td><a href="http://www.jjwdesign.com/">JJW Design</a></td>
#<td><a href="http://www.iproundup.com/">IP Roundup</a></td>
#</tr>
#</table>


import os
import sys

import urlparse, urllib

#def path2url(path):
#	return urlparse.urljoin('file:', urllib.pathname2url(path))
	  

# fileList = []
# fileSize = 0
# folderCount = 0



import subprocess
import os


import shutil

totalpdfs = 0
for root, subFolders, files in os.walk( ur'.' ):
	for file in files:
		if ( '.jpg' in file ):
			continue
		if ( 'age_game' in file ):
			continue
		if ( '.pdf' not in file ):
			continue
		totalpdfs += 1
		
		f = os.path.join(root,file)
		
		f2 = os.path.join(root, str(totalpdfs)+'_age_game.pdf')
		shutil.copy(f, f2)
		
		# print f
		# print repr(file)


for root, subFolders, files in os.walk( ur'.' ):
	for file in files:
		if ( '.jpg' in file ):
			continue
		if ( '.pdf' not in file ):
			continue
		if ( 'age_game' not in file ):
			continue
		
		f = os.path.join(root,file)
		# nconvert.exe -overwrite -out jpeg -thumb 100 100 abc.pdf
		cmd = 'nconvert.exe -overwrite -out jpeg -thumb 200 200 "' + f + '"'
		
		proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
		alfa = proc.communicate()[0]
		print('------\n')

list = []		

for root, subFolders, files in os.walk( ur'.' ):
	#folderCount += len(subFolders)
	for file in files:
		
		if ( ".py" in file ):
			continue
		
		if ( '.pdf' not in file ):
			continue
		if ( '.jpg' in file ):
			continue
		
		if ( 'age_game' not in file ):
			continue
			
		f = os.path.join(root,file)
		
		# fileSize = fileSize + os.path.getsize(f)
		#print(f)
		#fileList.append(f)
		filename = file
		
		# f = urllib.pathname2url( f )
		
		fjpg = f[:-4] + '.jpg'
		list.append( [f, fjpg] )
		
		# ss = "<a href=\"" + f + "\">" + filename + "</a><br> \n"
		# fp.write(ss)


fp = open("index.html", "w")
fp.write("""
<html>
<head>
	<style type="text/css">
	table
	{ 
	margin-left: auto;
	margin-right: auto;
	}
	table { border: 0px solid black }
	td { border: thin solid black }
	</style>
</head>
<body>

<table cellpadding="10">
<tr>
""");



for i in range(0,len(list) ):
	a = list[i]
	
	pdffilename = a[0]
	jpgfilename = a[1]
	
	pdffilename = urllib.pathname2url( pdffilename )
	jpgfilename = urllib.pathname2url( jpgfilename )

	ss = ""
	if ( i % 5 == 0 ):
		ss += "</tr><tr>"
		
	ss += '<td><a href="'+pdffilename+'"><img src="'+jpgfilename+'"></a></td>'
	ss += "\n"
	


	# ss = "<a href=\"" + f + "\">" + filename + "</a><br> \n"
	fp.write(ss)
		
fp.write("""
</tr>
</table>

</body></html>
""")
fp.close()
fp = 0

# print("Total Size is {0} bytes".format(fileSize))
# print("Total Files ", len(fileList))
# print("Total Folders ", folderCount)

