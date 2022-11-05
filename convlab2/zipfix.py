import zipfile

def fix_zip_file(zipFileContainer):
    # Read the contents of the file
    content = zipFileContainer.read()
    pos = content.rfind(b'\x50\x4b\x05\x06')  # reverse find: this string of bytes is the end of the zip's central directory.
    if pos>0:  # Double check we're not at the beginning of the file so we don't blank out the file
        zipFileContainer.seek(pos+20)  # Seek to +20 in the file; see secion V.I in 'ZIP format' link above.
        zipFileContainer.truncate()  # Delete everything that comes after our current position in the file (where we `seek` to above).
        zipFileContainer.write(b'\x00\x00') # Zip file comment length: 0 byte length; tell zip applications to stop reading.
        zipFileContainer.seek(0)  # Go back to the beginning of the file so the contents can be read again.

    return zipFileContainer
  
def getzipfilecontainer(path):
  zipfilecontainer = open(path,'r+b')
  return zipfilecontainer

def getfixedzip(path):
  zipfilecontainer = getzipfilecontainer(path)
  fixedzipfile = fix_zip_file(zipfilecontainer)
  return fixedzipfile
