import sys
import re

'''
This is to create a vcf file after all the repeated phone numbers are removed, which might be 
in different VCARD or duplicated within the same VCARD

Sometimes, in android phones somehow the numbers get duplicated, and we can't find any option to remove extras

To run, export contacts as vcf, then
$ python removeDup.py contacts.vcf > out.vcf

Then copy it back to phone, delete all the contacts, and import out.vcf
'''
def main():
    fname = "contacts.vcf"
    
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    
    uniq = []   # final contact list that contains entries having unique phone numbers
    numlst = [] # list having all the phone numbers seen
    
    with open(fname, "r") as fo:
        content = fo.read()
        spl = content.split("BEGIN:VCARD")
    
        for s in spl:
            lines = s.split("\n")
            uniqlst = []                  # list containing the split contact entry
            addentry = False              # add the entry only if a new number is found in the split list
            for l in lines:
                if l.find("PHOTO") == -1: # don't look inside base64 encoded characters
                    num1 = re.findall(r"\d+\-\d+\-\d+", l)
                    num2 = re.findall(r"\+?\d{10,12}", l) 
                else:
                    num1, num2 = [], []
                    
                if not (num1 + num2):
                    uniqlst.append(l)
                if num1 and num1[0] not in numlst:
                    numlst += num1
                    uniqlst.append(l)
                    addentry = True
                if num2 and num2[0] not in numlst:
                    numlst += num2
                    uniqlst.append(l)
                    addentry = True
    
            if addentry:
                uniq.append("\n".join(uniqlst))
    
    return "BEGIN:VCARD" + "BEGIN:VCARD".join(uniq)

if __name__ == "__main__":
    print(main())
    
