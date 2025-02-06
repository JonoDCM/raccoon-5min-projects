from sklearn import tree

# [height, weight, shoe size]
X = [[181,80,44], [175,70,43], [167,60,40], [160,60,37],
	 [166,65,41], [177,85,42], [181,64,44], [165,75,38],
	 [171,70,42], [169,90,39], [179,74,42]

Y = ['male', 'male', 'female', 'female', 
 	 'female', 'female', 'male', 'female', 
 	 'male', 'male', 'female']

#store DeciscionTreeClassifier (clf = Classifier)
clf = tree.DeciscionTreeClassifier()

#results will be stored in clf after its value updates
clf = clf.fit(X,Y)

#prediction is where we store the result of ^
#call predict method of our deciscion tree to predict the gender off the 3 values in the list
prediction = clf.predict([[190,80,50]])

print prediction
