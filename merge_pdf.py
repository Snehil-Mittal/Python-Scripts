# PyPDF2 deals with functions related to text-based pdf
import PyPDF2,os 
print ("Welcome to the Pdf Merger...")
# Creating a list so as to store all the pdf files in our present directory
pdfFile = []
for filename in os.listdir('.'):
# os.listdir('.') function provides us with all the files in the directory one by one 
    if filename.endswith('.pdf'): 
    # Checking which files are actually pdfs in our directory
        pdfFile.append(filename)
        # Adding those found files into our list created
pdfFile.sort(key=str.lower)
# Sorting the pdf files in the list
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFile:
    pdfReader=PyPDF2.PdfFileReader(open(filename,'rb'))
    # The following is the code of Decryption and runs if any encrypted files to be merged is present in the directory
    if pdfReader.isEncrypted:
        print (filename,"is encrypted.")
        password =  input("Enter the password to decrypt: ")
        pdfReader.decrypt(password)
    for pageNum in range(0,pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        pdfWriter.addPage(page)
result = open('final.pdf','wb')
# To add encryption to the merged pdf
choice = input("Do you want to add any encryption to the resulting pdf, yes/no: ")
if choice == "yes":
    newpassword= input("Enter the password: ")
    pdfWriter.encrypt(newpassword)
pdfWriter.write(result)
result.close()
# Closing the output file after writing the pages in it