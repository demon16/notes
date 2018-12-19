import tensorflow as tf

classifier = tf.estimator.LinearClassifier()

classifier.train(input_fn=tran_input_fn, setps=2000)

predictions = classifier.predict(input_fn=predict_input_fn)