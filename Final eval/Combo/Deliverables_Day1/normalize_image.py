import os, sys
import Image,ImageOps

size = 16, 8
'''
for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile'''
			
for path, subdirs, files in os.walk("./Images/"):
	if(not path.endswith("ConvertedImages")):
		i=0
		for file in files:
			#print path+"/ConvertedImages/"+file
			outfile = path+"/ConvertedImages/"+str(i)+".jpg"
			i += 1
			infile = path+"/"+file
			try:
				im = Image.open(infile)
				#im.resize(size)
				img = ImageOps.fit(im, size, Image.ANTIALIAS)
				img.save(outfile, "JPEG")
			except IOError:
				print "cannot create thumbnail for '%s'" % infile