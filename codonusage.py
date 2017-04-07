''' The code was written using Python3.'''

# ==============================================================================================================
'''
 Input - A Fasta file named 'sequence.fasta'.
 Output - Frequencies of all codons on command line.
'''
# ==============================================================================================================

def codon_usage_table(temp, codon_freq, codon_table):
    
    ''' This function converts the result which is in dictionary format for display in string format '''

    for i in temp.keys():
        print(i+"-"+codon_table[i]+"  "+str(codon_freq[i]))   # prints the final output
        

def codon_counter(codons, no_of_codons, codon_table):

    ''' This function count the no. of codon and stores the output in codon_freq while temp contains the nested
        dictionary containing the information of codon, amino acid and frequency. '''

    codon_freq = {} ; temp ={}
    for i in codons:
        if not i in codon_freq:
            codon_freq[i] = round(float(codons.count(i))/no_of_codons * 1000,4)   # calculates frequency of each codon       
    for i in codon_freq.keys():
        temp[i] = dict()
        temp[i][codon_table[i]] = codon_freq[i]
    codon_usage_table(temp, codon_freq, codon_table)	   

                    
def codon_creater(read, codon_table):

    ''' This function takes the fasta file in string format 'read' and converts it to a list 'codons' where each
    element is a codon '''

    codons = []
    for i in range(0,len(read),3):          # creates a triplet codon 
        codons.append(read[i:i+3])
    no_of_codons = len(codons)    
    codon_counter(codons, no_of_codons, codon_table)    

        
codon_table={'UUU':'Phe','CUU':'Leu','AUU':'Ile','GUU':'Val','UUC':'Phe','CUC':'Leu','AUC':'Ile','GUC':'Val',
'UUA': 'Leu', 'CUA':'Leu', 'AUA':'Ile','GUA':'Val','UUG':'Leu','CUG':'Leu','AUG':'Met','GUG':'Val',
'UCU':'Ser','CCU':'Pro','ACU':'Thr','GCU': 'Ala','UCC':'Ser','CCC':'Pro','ACC':'Thr','GCC':'Ala',
'UCA': 'Ser','CCA':'Pro','ACA':'Thr','GCA':'Ala','UCG':'Ser','CCG':'Pro','ACG':'Thr','GCG':'Ala',
'UAU': 'Tyr', 'CAU': 'His','AAU':'Asn','GAU':'Asp','UAC':'Tyr','CAC':'His','AAC':'Asn', 'GAC': 'Asp',
'UAA':'TER','CAA':'Gln','AAA':'Lys','GAA':'Glu','UAG':'TER','CAG':'Gln','AAG':'Lys','GAG':'Glu',
'UGU': 'Cys', 'CGU':'Arg','AGU':'Ser','GGU':'Gly','UGC':'Cys','CGC': 'Arg','AGC':'Ser','GGC':'Gly',
'UGA':'TER','CGA':'Arg','AGA':'Arg','GGA':'Gly','UGG':'Trp','CGG':'Arg','AGG': 'Arg','GGG':'Gly'}

def main():
    
    ''' It opens the file and converts it to 'read' which is the genomic sequence in string format.'''

    f = open("input_codonusage.fasta","r")
    r = f.readlines()
    t = [i.rstrip("\n") for i in r]
    nos = t.count("")
    for i in range(nos):                     # removes spaces in the list 't'.
        t.remove("")
    temp = "";read = ""; seq = []   
    for i in range(len(t)):                  # creates a list 'seq' with file header and sequence occupying alternate positions. 
        if t[i][0] == ">":
            if len(temp) != 0:
                seq.append(temp)
                temp = ""
            else:
                pass
            seq.append(t[i])
        else:
            temp += t[i]
            if i == len(t) - 1:
                seq.append(temp)
    reads = [seq[i] for i in range(len(seq)) if i%2 != 0]
    for i in range(len(reads)):             # 'read' is whole sequence in string format. 
        read += reads[i]
    read = read.replace('T','U')            # replace 'T' with 'U' in read. 
    codon_creater(read, codon_table)

main()
