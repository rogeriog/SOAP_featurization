## this file will download the datafiles necessary to the investigation.
import gdown, tarfile, os
import gzip, shutil
def extract_targz(filename,outputname):
    with open(filename,"rb") as file:
        tfile = tarfile.open(fileobj=file)
        tfile.extractall(outputname)
        tfile.close()
    os.remove(filename)

def extract_gz(filename,outputname):
    with gzip.open(filename, 'r') as f_in, open(outputname, 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)    
    os.remove(filename)


url = 'https://drive.google.com/uc?id=1Stq1_eUN8z58tbozq5-tPfyNJEdMz7XQ'
output = './DATAFILES/matbench_mp_gap_light.gz'
#gdown.download(url, output, quiet=False)
#extract_gz(output,'./DATAFILES/matbench_mp_gap_light')

url = 'https://drive.google.com/uc?id=1SxOb0Aauq2tFCJIdzwHB5Qd7Eo90rx03'
output = './DATAFILES/matbench_mp_gap_matminer.pkl'
#gdown.download(url, output, quiet=False)

