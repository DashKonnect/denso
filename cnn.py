import tensorflow as tf 

training_data = []
file_name = 'training_data.npy'
if os.path.isfile(file_name):
	print('File exists, loading previous data!')
	training_data = list(np.load(file_name))

X = np.array([i[0] for i in training_data])
X = scale( X, axis=0, with_mean=True, with_std=True, copy=True )
Y = np.array([int(i[1]) for i in training_data])

