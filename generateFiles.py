import os
from os.path import exists, join, basename, splitext

directory = "./Videos/"
processed_output = "./Processed/"
Output_CSV = "./Output_CSV/"

for filename in os.listdir(directory):
        file_name = os.path.join(directory, filename)
        os.system("./opencv-4.1.0/build/OpenFace/build/bin/FeatureExtraction -f %s -out_dir %s"%(file_name, processed_output))
        outFileName_str = filename.split(".")[0] + ".csv"
        outFileName = os.path.join(processed_output, outFileName_str)
        os.system("mv %s %s"%(outFileName, Output_CSV))
        os.system("rm -rf %s*"%(processed_output))
