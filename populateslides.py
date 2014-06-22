import codecs
import os
import glob

dirname = "parosprep/"

fo = codecs.open("imgs_body.txt", 'w')
krange = range(1, 114)
os.chdir(dirname)
for k in krange:
    for fname in glob.glob('{0}.jpg'.format(k)):

        fo.write('<img src="' + dirname + fname +
                 '" class="img-responsive">\n')

os.chdir('..')

fo.close()
