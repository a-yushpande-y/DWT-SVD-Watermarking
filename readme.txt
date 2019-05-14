######################### README #####################################

Software requirements:
1) Python 2.7 (Download from https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi)

Additional modules required:
1)Numpy
2)OpenCV
3)pywt

Environment Setup:
1)Go to the Environment Variables tab, you do this by pressing Windows key + Pause or by right clicking on my computer and going to properties.
2)Go to Advanced System Settings.
3)Click on Environment Variables.
3)On the lower window search for the 'Path' value.
4)Select it
5)Click on Edit
6)In the end of the line add your instalation folder (For example: C:\python27) and also the route to 'Scripts' folder (For example: C:\python27\Scripts).
7)Click ok, apply etc.

Install Additional modules:
1)Open command prompt in administrator mode.
2)Run the command 'pip install numpy', 'pip install opencv-python', 'pip install pywt'(all without the quotes)


How to embed watermark:
1)Right click on the file main.py and select Edit in IDLE
2)The file will open in IDLE 
3)Go to the navigation bar and under the dropdown Run, click on Run module or simply press F5.
4)The code will start the execution
5)First it will ask for the path of the watermark image. Input it.(baboon256.jpg in our case)
6)Then it will ask for the system parameters X(0) and u. Enter them in the specified range.
7)The code will then ask two prime numbers for the RSA part. Enter them and the private and public key will be generated. Remember the public key for further use.
8)Then input the path of the host image. (lena512.jpg in our case)
9)It will do the embedding and store the images in the images folder.
10)Press enter to start the extraction
11)Right click on the file decryption.py and select Edit in IDLE
12)The file will open in IDLE 
13)Go to the navigation bar and under the dropdown Run, click on Run module or simply press F5.
14)The code will start the execution
15)First it will ask for the path of the original image. Input it.(lena512.jpg in our case)
16)Then it will ask for the path of the watermarked image. Input it.(images/watermarked_image.jpg in our case)
17)Then it will ask the public key for the decryption of system parameters.
18)The watermark will be recovered and stored in the images folder.
