from os import listdir
from os.path import isdir
from PIL import Image
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN

faces = list()
directory = '5-celebrity-faces-dataset/train/'
# enumerate files
for filename in listdir(directory):
    
    # path
    path = directory + filename
    # get face
    face = extract_face(path)
    # store
    faces.append(face)

print(faces)


##def load_dataset(directory):
##	X, y = list(), list()
##	# enumerate folders, on per class
##	for subdir in listdir(directory):
##		# path
##		path = directory + subdir + '/'
##		# skip any files that might be in the dir
##		if not isdir(path):
##			continue
##		# load all faces in the subdirectory
##		faces = load_faces(path)
##		# create labels
##		labels = [subdir for _ in range(len(faces))]
##		# summarize progress
##		print('>loaded %d examples for class: %s' % (len(faces), subdir))
##		# store
##		X.extend(faces)
##		y.extend(labels)
##	return asarray(X), asarray(y)
##    
##trainX, trainy = load_dataset('5-celebrity-faces-dataset/train/')
##print(trainX.shape, trainy.shape)
