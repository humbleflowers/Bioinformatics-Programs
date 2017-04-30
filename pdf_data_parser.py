# Author - Vinay RK
# The following scipt was written on Ubuntu OS using Python version 2.7

import re, os, openpyxl, csv

def pdf_to_txt():
	inp = 'ALL.pdf'
	out = 'ALL.txt'
	os.system(("ps2ascii %s %s") %(inp, out))

def data_parser(headings):
	ls_split=[]
	f = open('ALL.txt')
	flist = [line.rstrip() for line in f]
	#print flist
	flist = [i for i in flist if i!= '']
	fstr= ' '.join(flist)
	#print fstr 	
	start = re.escape("!\"#$%&#'%()*")   
	end = re.escape('*G$*=:')
	fstr = re.sub('%s(.*?)%s' %(start,end),' ',fstr) #removing footer
	entries=[]
	for i in range(len(headings)-1):
		entries.append(re.findall(r'%s(.*?)%s'%(headings[i],headings[i+1]), fstr))   # collecting the data for all the headers
	entries.append(re.findall(r'%s(.*?)%s'%('Notes:','Disease Description:'),fstr)) # collecting data for Notes heading
	return entries # contains all the required data in the form of list for every header

def result_in_txt(entries):
	fw = open('result.txt','w')
	for i in headings:
		fw.write(str(i)+'\t')
	fw.write('\n')
	data=[]
	for cols in zip(*entries):
		data.append(cols)  # create the columns
	for i in range(len(data)):
		for j in range(len(data[i])):
			fw.write(str(data[i][j])+'\t') # write in txt file in coorrect order
		fw.write('\n')	

def text_to_xl():
	inp_file='result.txt'
	out_file='result.xlsx'
	bw = openpyxl.Workbook()
	sw = bw.worksheets[0]
	with open(inp_file,'rb') as data:
		reader = csv.reader(data, delimiter='\t') #define delimiter and write in excel sheet
   		for row in reader:
        		sw.append(row)
	bw.save(out_file)

headings = ['Disease Description:','Specific Indication:','Molecular Abnormality:','Test:','Chromosome:','Gene Symbol:','Test Detects:','Methodology:','NCCN Category of Evidence:','Specimen Types:','NCCN Recommendation - Clinical Decision:','Test Purpose:','When to Test:','Guideline Page with Test Recommendation:','Notes:']
		
pdf_to_txt()
entries=data_parser(headings)
result_in_txt(entries)
text_to_xl()

print "========== The Program was excuted. Please check result.xlxs ============\n"
