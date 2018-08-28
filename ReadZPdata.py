# This is a script for reading Zip record

import os;
import random;

# 
src = "E:/data";
OutputSrc = "E:/sample_data"
if os.path.exists(OutputSrc):
    print "files exists";
else:
    os.makedirs(OutputSrc);

subfolders = os.listdir(src);
print "There is %d subfloders" % len(subfolders);

for subf in subfolders:
    files = os.listdir(src + '/'+ subf);
    print "There is %d files need to read" % len(files);
    for fileName in files:
        fobj = open(src + '/' + subf + '/' + fileName,"r");
        # tempData is the string format
        tempData = fobj.read();
        # ZPdata is key-value 
        ZPdata = eval(tempData);
        print fileName,
        print ": %d ZP records" % len(ZPdata);

        print "Obtaining the random sample.."
        # we just need 20% ZPdata
        sampleNum = int(len(ZPdata)/5);
        
        ZP_key = ZPdata.keys();

        # build an Empty key value
        ZPdataSample = {};
        for i in range(sampleNum):
            ZPdataSample[ZP_key[i]] = ZPdata[ZP_key[i]];
        
        # write the Sample to the TextFile
        if os.path.exists(OutputSrc + '/' + subf):
            print "folder exists";
        else:
            os.makedirs(OutputSrc + '/' + subf);
            
        f2 = open(OutputSrc + '/' + subf + '/sub_' + fileName,"w");
        f2.write(str(ZPdataSample));
        f2.close();
            
        fobj.close();

   
